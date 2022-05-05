import math

from simulator.flyobj import *
from simulator.stage import *


class Rocket(FlyObject):
    mass_fuel = 0.0
    head = 0.0
    engine_on = False

    width = 0.0
    height = 0.0

    fuel_eff = 0.0
    fuel_flow_rate = 0.0

    t = 0
    mode = 0

    stages = []

    # TODO: initialize stages with configuration
    def __init__(self, name, mass, x, y, vx, vy, fuel_eff, fuel_flow_rate):
        super().__init__(name, mass, x, y, vx, vy)

        self.stages = [
            Stage('Stage 1', 2, 80, 800, 0.5),
            Stage('Stage 2', 1, 40, 400, 0.25)
        ]

        self.radius = 20

    def initImages(self, engineOffImage, engineOnImage):
        self.image = image.load(engineOffImage)
        self.imageEngine = image.load(engineOnImage)

        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def flightProgram(self):
        pass

    def setFuel(self, mass):
        # TODO: Change how we configure fuel for each stage
        self.mass_fuel = mass
        print("Fuel added:", mass)

    def getMass(self):
        stagesMass = 0.0
        for stage in self.stages:
            stagesMass += stage.getMass()
        return self.mass + stagesMass

    def getReactiveAccel(self):
        currentStage = self.getCurrentStage()
        if currentStage is None:
            return 0
        return currentStage.getFuelEfficiency() / self.getMass()

    def fx(self, x):
        a = super().fx(x)
        if self.isEngineOn():
            a += math.sin(math.radians(self.head)) * self.getReactiveAccel()
        return a

    def fy(self, y):
        a = super().fy(y)
        if self.isEngineOn():
            a -= math.cos(math.radians(self.head)) * self.getReactiveAccel()
        return a

    def update(self):
        super().update()
        self.t += T
        
        currentStage = self.getCurrentStage()
        if currentStage is None:
            return

        if currentStage.hasFuel() and self.isEngineOn():
            currentStage.engineOn()

        if currentStage.hasFuel() and not self.isEngineOn():
            currentStage.engineOff()

        if not currentStage.hasFuel():
            print('Lack of fuel')
            self.dropStage()

        currentStage.update()

    def draw(self, screen, zoom, dx, dy):
        if self.isEngineOn():
            img = self.imageEngine
        else:
            img = self.image

        new_x = int((self.x - self.width // 2) * zoom + dx)
        new_y = int((self.y - self.height // 2) * zoom + dy)

        screen.blit(transform.rotozoom(img, (-1) * self.head, zoom), (new_x, new_y))

    def getSize(self):
        return max(self.image.get_width()//2, self.image.get_height()//2)

    def setHead(self, head):
        self.head = head

    def getHead(self):
        print("Head: {0:6.1f}".format(self.head))
        return self.head

    def engineOn(self):
        self.engine_on = True
        if self.hasStages():
            self.getCurrentStage().engineOn()
        print("Engine is ON at: {0:6.2f}".format(self.t))

    def engineOff(self):
        self.engine_on = False
        if self.hasStages():
            self.getCurrentStage().engineOff()
            print("Engine is OFF at: {0:6.2f}, fuel left {1:6.2f}".format(self.t, self.getCurrentStage().mass_fuel))

    def isEngineOn(self):
        if not self.engine_on:
            return False

        if not self.hasStages():
            return False

        return self.getCurrentStage().hasFuel()

    def hasStages(self):
        return len(self.stages) != 0

    def getCurrentStage(self):
        if not self.hasStages():
            return None
        return self.stages[0]

    def dropStage(self):
        if not self.hasStages():
            return
        print('Drop ' + self.getCurrentStage().name + ' at: {0:6.2f}'.format(self.t))
        self.stages.pop(0)
