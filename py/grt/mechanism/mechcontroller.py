import math
import time
from wpilib import CANTalon

class MechController:

    def __init__(self, driver_joystick, xbox_controller, turn_1, turn_2, turn_3, turn_4): # mechanisms belong in arguments
        # define mechanisms here

        self.turn_1 = turn_1
        self.turn_2 = turn_2
        self.turn_3 = turn_3
        self.turn_4 = turn_4

        self.driver_joystick = driver_joystick
        self.xbox_controller = xbox_controller
        driver_joystick.add_listener(self._driver_joystick_listener)
        xbox_controller.add_listener(self._xbox_controller_listener)

    def _xbox_controller_listener(self, sensor, state_id, datum):
        if state_id == 'a_button':
            if datum:

                self.turn_1.setEncPosition(0)
                self.turn_2.setEncPosition(0)
                self.turn_3.setEncPosition(0)
                self.turn_4.setEncPosition(0)


                self.turn_1.set(0)
                self.turn_2.set(0)
                self.turn_3.set(0)
                self.turn_4.set(0)


    def _driver_joystick_listener(self, sensor, state_id, datum):
        pass