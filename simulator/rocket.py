import pygame as pygame

from simulator.flyobj import *
from simulator.stage import *


class Rocket(FlyObject):
    mass_fuel = 0.0
    head = 0.0
    engine_on = False

    width = 0.0
    height = 0.0

    t = 0
    tick = 0
    mode = 0
    coordinates = []


    def __init__(self, name, mass, x, y, vx, vy, stages):
        super().__init__(name, mass, x, y, vx, vy)

        self.stages = stages

        self.radius = 20

    def initImages(self, engineOffImage, engineOnImage):
        self.image = image.load(engineOffImage)
        self.imageEngine = image.load(engineOnImage)

        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def flightProgram(self):
        pass

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
        self.tick += 1
        
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

        if len(self.coordinates) > 2:
            for i in range(1, len(self.coordinates)):
                PINK = (255, 192, 203)
                pygame.draw.lines(screen, PINK, False, self.coordinates, 2)

        if self.tick % 100 == 0:
            self.coordinates.append((new_x, new_y))

        font = pygame.font.SysFont('Arial', 20)
        text_surface = font.render('Tick {0}, time {1}'.format(self.tick, self.t), False, (255, 255, 255))
        screen.blit(text_surface, (20, 20))

    def getSize(self):
        return max(self.image.get_width()//4, self.image.get_height()//4)

    def setHead(self, head):
        self.head = head

    def getHead(self):
        return self.head

    def engineOn(self):
        self.engine_on = True
        if self.hasStages():
            self.getCurrentStage().engineOn()
        print("Engine is ON at: {0:6.3f}".format(self.t))

    def engineOff(self):
        self.engine_on = False
        if self.hasStages():
            self.getCurrentStage().engineOff()
            print("Engine is OFF at: {0:6.3f}, fuel left {1:6.3f}".format(self.t, self.getCurrentStage().mass_fuel))

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
        print('Drop ' + self.getCurrentStage().name + ' at: {0:6.3f}'.format(self.t))
        self.stages.pop(0)
