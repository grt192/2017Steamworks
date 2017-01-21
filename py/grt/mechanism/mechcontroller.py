import math
import time
from wpilib import CANTalon

class MechController:

    def __init__(self, driver_joystick, xbox_controller, shooter, intake, climber, gear, hopper): # mechanisms belong in arguments
        # define mechanisms here

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
                self.hopper.unjam_out()
            else:
                self.hopper.unjam_in()

        elif state_id == 'b_button':
            if datum:
                self.gear.place()
            else:
                self.gear.retract()

        elif state_id == 'x_button':
            if datum:
                self.intake.intake()

        elif state_id == 'y_button':
            if datum:
                self.intake.stop()
                
        elif state_id == 'r_shoulder': #needs review
            if datum:
                self.gear.unjam_up()
            else:
                self.gear.unjam_down()
                
        elif state_id == 'l_shoulder': #needs review
            if datum:
                self.climber.climb()
            else:
                self.climber.stop()

        elif state_id == 'r_trigger':
            if datum:
                self.shooter.ramp_up_speed(33000,33000)

        elif state_id == 'l_trigger':
            if datum:
                self.shooter.ramp_up_speed(0,0)

        elif state_id == 'r_y_axis':
            if datum:
                self.shooter.shoot()
            else:
                self.shooter.stop()

        elif state_id == 'start_button':
            if datum:
                self.shooter.angle_change_up()

        elif state_id == 'back_button':
            if datum:
                self.shooter.angle_change_down()

            

    def _driver_joystick_listener(self, sensor, state_id, datum):
        
        pass