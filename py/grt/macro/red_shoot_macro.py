
__author__ = 'alex gao'

import threading
from grt.core import GRTMacro
import time
import math

class RedShootMacro(GRTMacro):

    POWER = 0.4

    SPEED = 2550

    def __init__(self, swerve, shooter, intake, timeout=None):
        super().__init__()
        self.swerve = swerve
        self.shooter = shooter
        self.intake = intake
        #self.enabled = False

        #self.abort = False


    def abort(self):
        self.abort = True

    def initialize(self):


        print("initialized red shoot")
        self.shooter.angle_change_up()
        self.shooter.ramp_up_speed(self.SPEED, self.SPEED)
        time.sleep(1)
        self.shooter.shoot()
        self.intake.intake()

        time.sleep(9)

        print("DONE SHOOTING")

        self.shooter.stop()
        self.shooter.ramp_down_to_zero()
        self.shooter.angle_change_down()
        self.intake.stop()

        #self.enable()

        print("STRAFING")
        print("STRAFING")
        print("STRAFING")
        print("STRAFING")
        self.swerve.strafe(0, 0, 1)
        time.sleep(1)
        
        self.swerve.strafe(0,1,self.POWER)
        time.sleep(2.5)
        
        self.kill()
        self.die()
        

    def enable(self):
        self.enabled = True
        


    def disable(self):
        #self.swerve.ackerman_turn(0, 0)
        #self.swerve.strafe(0, 0, 1)
        self.swerve.set_power(0)
        print("straight swerve disabled")
        #self.abort()
        #self.enabled = False
        
    def die(self):
        self.disable()
        


    

