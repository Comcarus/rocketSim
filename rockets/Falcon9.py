from simulator.rocket import Rocket

class SmoothOrbiter(Rocket):
    def flightProgram(self):
        if self.mode == 0:
            self.engineOn()
            self.mode = 1

        if 1 <= self.t <= 161 and self.mode == 1:
            self.setHead(self.getHead() + .5)

        if self.t > 162 and self.mode == 1:
            self.engineOff()
            self.mode = 2
        
        if self.t > 163 and self.mode == 2:
            self.engineOn()
            self.mode = 3

        if self.t > 561 and self.mode == 3:
            self.engineOff()
            self.mode = 4

class SmoothOrbiter1(Rocket):
    def flightProgram(self):
        if self.mode == 0:
            self.engineOn()
            self.mode = 1

        if 0.1 <= self.t <= 16.1 and self.mode == 1:
            self.setHead(self.getHead() + .5)

        if self.t > 16.2 and self.mode == 1:
            self.engineOff()
            self.mode = 2
        
        if self.t > 16.3 and self.mode == 2:
            self.engineOn()
            self.mode = 3

        if self.t > 56.1 and self.mode == 3:
            self.engineOff()
            self.mode = 4

class SmoothOrbiter2(Rocket):
    def flightProgram(self):
        if self.mode == 0:
            self.engineOn()
            self.mode = 1

        if 0.01 <= self.t <= 1.61 and self.mode == 1:
            self.setHead(self.getHead() + .5)

        if self.t > 1.62 and self.mode == 1:
            self.engineOff()
            self.mode = 2
        
        if self.t > 1.63 and self.mode == 2:
            self.engineOn()
            self.mode = 3

        if self.t > 5.61 and self.mode == 3:
            self.engineOff()
            self.mode = 4

class SmoothOrbiter3(Rocket):
    def flightProgram(self):
        if self.mode == 0:
            self.engineOn()
            self.mode = 1

        if 0.001 <= self.t <= 0.161 and self.mode == 1:
            self.setHead(self.getHead() + .5)

        if self.t > 0.162 and self.mode == 1:
            self.engineOff()
            self.mode = 2
        
        if self.t > 0.163 and self.mode == 2:
            self.engineOn()
            self.mode = 3

        if self.t > 0.561 and self.mode == 3:
            self.engineOff()
            self.mode = 4