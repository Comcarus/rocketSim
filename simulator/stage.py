# TODO: remove duplication of variables with rocket.py
T = .05


class Stage:
    mass = 0.0
    mass_fuel = 0.0
    is_on = False
    fuel_eff = 0.0
    fuel_flow_rate = 0.0

    t = 0
    mode = 0

    def __init__(self, name, mass, mass_fuel, fuel_eff, fuel_flow_rate):
        self.name = name
        self.mass = mass
        self.mass_fuel = mass_fuel
        self.fuel_eff = fuel_eff
        self.fuel_flow_rate = fuel_flow_rate

    def update(self):
        self.t += T

        if self.isEngineOn():
            self.mass_fuel -= self.fuel_flow_rate
            # print("Stage {stage} is on fuel: {fuel}".format(stage=self.name, fuel=self.mass_fuel))

    def hasFuel(self):
        return self.mass_fuel > 0

    def getMass(self):
        return self.mass + self.mass_fuel

    def getFuelEfficiency(self):
        return self.fuel_eff * self.fuel_flow_rate

    def engineOn(self):
        self.is_on = True
        #print("{name} is ON at: {time:6.2f} flight time".format(name=self.name, time=self.t))

    def engineOff(self):
        self.is_on = False
        #print("{name} is OFF at: {time:6.2f} flight time, fuel left {fuel:6.2f}".format(name=self.name,time=self.t, fuel=self.mass_fuel))

    def isEngineOn(self):
        return self.is_on and self.mass_fuel > 0
