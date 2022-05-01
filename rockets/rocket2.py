from simulator.rocket import Rocket

class MoonFlyer(Rocket):
    def flightProgram(self):
        #Take off and turn 90" right
        if self.mode == 0:
            self.engineOn()
            self.mode = 1

        if self.t > 12.0 and self.mode == 1:
            self.engineOff()
            self.setHead(90)
            self.mode = 2

        #Go to round orbit
        if self.t > 20 and self.mode == 2:
            self.engineOn()
            self.mode = 3

        if self.t >= 26 and self.mode == 3:
            self.engineOff()
            self.mode = 4

        if self.t >= 150 and self.mode == 4:
            self.engineOn()
            self.mode = 5

        if self.t >= 155 and self.mode == 5:
            self.engineOff()
            self.mode = 6

        if self.t >= 185 and self.mode == 6:
            self.setHead(270)
            self.mode = 7

        if self.t >= 190 and self.mode == 7:
            self.engineOn()
            self.mode = 8

        if self.t >= 195 and self.mode == 8:
            self.engineOff()
            self.mode = 9

        if self.t >= 210 and self.mode == 9:
            self.setHead(180)
            self.mode = 10

        if self.t >= 214 and self.mode == 10:
            self.engineOn()
            self.mode = 11

        if self.t >= 215 and self.mode == 11:
            self.engineOff()
            self.mode = 12
