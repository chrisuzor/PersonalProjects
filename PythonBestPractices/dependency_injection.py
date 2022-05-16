from abc import ABC, abstractmethod


class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: turn on.....")

    def turn_off(self):
        print("LightBulb: turn off.....")


class ElectricPowerSwitch:
    def __init__(self, switch: Switchable):
        self.switch = switch
        self.on = False

    def press(self):
        if self.on:
            self.switch.turn_off()
        else:
            self.switch.turn_on()
            self.on = True


lightbulb = LightBulb()
switch = ElectricPowerSwitch(lightbulb)
switch.press()
switch.press()
