import math
import time
from ctre import CANTalon

class MechController:

    def __init__(self, driver_joystick, xbox_controller, shooter, intake, gear, hopper, climber=None, zero_test=None, talon_test=None): # mechanisms belong in arguments
        # define mechanisms here

        self.shooter = shooter
        self.intake = intake
        self.climber = climber
        self.gear = gear
        self.hopper = hopper

        self.zero_test = zero_test

        self.talon_test = talon_test

        self.front_power = 800#1500#2175 #OLD: 2150, 1000
        self.back_power = 1600#1500#4975 #OLD: 2150, 3100

        self.TIPPED = True

        self.driver_joystick = driver_joystick
        self.xbox_controller = xbox_controller
        driver_joystick.add_listener(self._driver_joystick_listener)
        xbox_controller.add_listener(self._xbox_controller_listener)

    def _xbox_controller_listener(self, sensor, state_id, datum):

        # if state_id == 'a_button':
        #     if datum:
        #         print("testing")
        #         self.talon_test.go_pneumatic(True)

        #     else:
        #         self.talon_test.go_pneumatic(False)


        # if state_id == 'r_shoulder': #GEAR ATM
        #     if datum:
        #         print("unjam hopper out")
        #         self.hopper.unjam_out()
        #     else:
        #         print("unjam hopper in")
        #         self.hopper.unjam_in()

        # if state_id == 'b_button':
        #     if datum:
        #         # self.power -= .01
        #         # print("POWER: ",self.power)
        #         print("placing gear")
        #         self.gear.place()
                
        #     else:
        #         print("gear back")
        #         self.gear.retract()

        if state_id == 'b_button':
            if datum:
                if self.TIPPED:
                    self.gear.place()
                    self.TIPPED = False
                else:
                    self.gear.retract()
                    self.TIPPED = True

        elif state_id == 'x_button':
            if datum:
                print("intaking")
                self.intake.intake()

        elif state_id == 'y_button':
            if datum:
                print("stopping intake")
                self.intake.stop()
                
        elif state_id == 'a_button': #needs review
            if datum:

                # self.power += .01
                # print("POWER: ",self.power)
                print("unjam gear down")
                self.gear.unjam_down()
            else:
                print("unjam gear up")
                self.gear.unjam_up()
                
                
        elif state_id == 'r_y_axis': #needs review
            if abs(datum) > .2:
                print("climbing")
                self.climber.climb_adjustable(datum)
            else:
                print("not climbing")
                self.climber.stop()

        elif state_id == 'l_y_axis': #needs review
            if abs(datum) > .2:
                print("climbing")
                self.climber.down()
            else:
                print("not climbing")
                self.climber.stop()

        elif state_id == 'l_trigger':
            if datum:
                print("ramp up shooter")
                self.shooter.ramp_up_speed(self.front_power,self.back_power) #48

        elif state_id == 'l_shoulder':
            if datum:
                print("stop shooter")
                self.shooter.ramp_down_to_zero()

        elif state_id == 'r_trigger':
            if datum:
                print("shooting")
                self.shooter.shoot()
            else:
                #print("not shooting")
                self.shooter.stop()

        elif state_id == 'start_button':
            if datum:
                print("achange up")
                self.shooter.angle_change_up()

        elif state_id == 'back_button':
            if datum:
                print("achanged downs")
                self.shooter.angle_change_down()

            

    def _driver_joystick_listener(self, sensor, state_id, datum):
        
        pass