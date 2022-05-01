from simulator.rocket import Rocket

class EarthOrbiter(Rocket):
    def flightProgram(self):
        #Take off and turn 90" right
        if self.mode == 0:
            self.engineOn()
            self.mode = 1

        if self.t > 12.0 and self.mode == 1:
            self.engineOff()
            self.setHead(90)
            self.mode = 2

        #Go to orbit
        if self.t > 20 and self.mode == 2:
            self.engineOn()
            self.mode = 3

        if self.t >= 26 and self.mode == 3:
            self.engineOff()
            self.mode = 4

class EllipseOrbiter(Rocket):
    def flightProgram(self):
        #Take off and turn 90" right
        if self.mode == 0:
            self.engineOn()
            self.mode = 1

        if self.t > 10.0 and self.mode == 1:
            self.engineOff()
            self.setHead(90)
            self.mode = 2

        #Go to orbit
        if self.t > 15 and self.mode == 2:
            self.engineOn()
            self.mode = 3

        if self.t >= 23 and self.mode == 3:
            self.engineOff()
            self.mode = 4

class SmoothhOrbiter(Rocket):
    def flightProgram(self):
        #Go to round orbit by smooth head increase
        if self.mode == 0:
            self.engineOn()
            self.mode = 1

        if 4.0 <= self.t <= 14 and self.mode == 1:
            self.setHead(self.getHead() + .6)

        if self.t > 15 and self.mode == 1:
            self.engineOff()
            #self.setHead(90)
            self.mode = 2