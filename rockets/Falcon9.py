from simulator.rocket import Rocket

class Smooth(Rocket):
    def flightProgram(self):
        if self.mode == 0:
            self.engineOn()
            self.mode = 1

        if 0.050 <= self.t <= 0.161 and self.mode == 1:
            self.setHead(self.getHead() + .5)

        if self.t > 0.162 and self.mode == 1:
            self.engineOff()
            self.mode = 2

        if self.t > 0.174 and self.mode == 2:
            self.engineOn()
            self.mode = 3

        if 0.175 <= self.t <= 0.530 and self.mode == 3:
            self.setHead(self.getHead() + .15)

        if self.getSpeed()>=7600 and self.mode == 3:
            self.engineOff()
            self.mode = 4

class BadRound(Rocket):
    def flightProgram(self):
        if self.mode == 0:
            self.engineOn()
            self.mode = 1

        if self.t > 0.162 and self.mode == 1:
            self.engineOff()
            self.setHead(90)
            self.mode = 2

        if self.t > 0.174 and self.mode == 2:
            self.engineOn()
            self.mode = 3

        if self.t > 0.527 and self.mode == 3:
            self.engineOff()
            self.mode = 4

class Round(Rocket):
    def flightProgram(self):
        if self.mode == 0:
            self.engineOn()
            self.mode = 1

        if self.t > 0.162 and self.mode == 1:
            self.engineOff()
            self.setHead(90)
            self.mode = 2
        
        if self.t > 0.173 and self.mode == 2:
            self.engineOn()
            self.mode = 3

        if self.vx>=7600 and self.mode == 3:
            self.engineOff()
            self.mode = 4
