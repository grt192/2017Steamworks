import math
import time
from wpilib import CANTalon

class MechController:

    def __init__(self, driver_joystick, xbox_controller, turn_1, turn_2, turn_3, turn_4, shooter, intake, climber, gear, hopper): # mechanisms belong in arguments
        # define mechanisms here

        self.turn_1 = turn_1
        self.turn_2 = turn_2
        self.turn_3 = turn_3
        self.turn_4 = turn_4

        self.shooter = shooter
        self.intake = intake
        self.climber = climber
        self.gear = gear
        self.hopper = hopper

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

        elif state_id == 'b_button':
            if datum:
                self.intake.intake()

        elif state_id == 'x_button':
            if datum:
                self.gear.retract()
                
        elif state_id == 'y_button':
            if datum:
                self.gear.place()

        elif state_id == 'r_shoulder': #needs review
            if datum:
                self.gear.unjam_up()
            else:
                self.gear.unjam_down()
                
        elif state_id == 'l_shoulder': #needs review
            if datum:
                self.hopper.unjam_out()
            else:
                self.hopper.unjam_in()

        elif state_id == 'r_trigger':
            if datum:
                self.climber.climb()

    def _driver_joystick_listener(self, sensor, state_id, datum):
        if state_id == 'trigger':
            if datum:
                self.shooter.ramp_up_speed(33000,33000) #not sure if these values are correct
            else:
                self.shooter.ramp_up_speed(0,0) #not sure if this will spin down the motors
                
        elif state_id == 'button2':
            if datum:
                self.shooter.shoot()

        elif state_id == 'button3':
            if datum:
                self.shooter.angle_change_up()
            else:
                self.shooter.angle_change_down()
