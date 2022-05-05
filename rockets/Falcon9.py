from simulator.rocket import Rocket

class RoundOrbiter(Rocket):
    def flightProgram(self):
        if self.mode == 0:
            self.engineOn()
            self.mode = 1

        # if 4.0 <= self.t <= 14 and self.mode == 1:
        #     self.setHead(self.getHead() + .6)

        if self.t > 162 and self.mode == 1:
            self.engineOff()
            self.mode = 2
        
        if self.t > 163 and self.mode == 2:
            self.engineOn()
            self.mode = 3

        if self.t > 560 and self.mode == 3:
            self.engineOff()
            self.mode = 4