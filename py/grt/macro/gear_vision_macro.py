import threading
from grt.core import GRTMacro
import time
import math


class GearVisionMacro(GRTMacro):

    POWER = 0.3

    SPEED = 2550

    def __init__(self, swerve,robot_vision, gear, timeout=None):
        super().__init__()
        self.swerve = swerve
        self.gear = gear
        self.robot_vision = robot_vision
        #self.enabled = False

        #self.abort = False


    def abort(self):
        self.abort = True

    def initialize(self):

        self.robot_vision.find_centers()

        

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