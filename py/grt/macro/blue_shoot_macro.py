
__author__ = 'alex gao'

import threading
from grt.core import GRTMacro
import time
import math

class BlueShootMacro(GRTMacro):

    POWER = 0.3

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


        print("initialized blue shoot")
        self.swerve.ackerman_turn(-2*math.pi/3, 0, 0)
        self.swerve.ackerman_turn(-2*math.pi/3, 0.6, 1)
        time.sleep(.5)
        self.swerve.set_power(0)
        self.shooter.angle_change_up()
        self.shooter.ramp_up_speed(self.SPEED, self.SPEED)
        time.sleep(1)
        self.shooter.shoot()
        self.intake.intake()

        time.sleep(8)

        print("DONE SHOOTING")

        self.shooter.stop()
        self.shooter.ramp_down_to_zero()
        self.shooter.angle_change_down()
        self.intake.stop()

        #self.enable()
        self.swerve.strafe(-5*math.pi/6, 0, 1)
        time.sleep(1)
        
        self.swerve.strafe(-5*math.pi/6,1,self.POWER)
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
        


    

