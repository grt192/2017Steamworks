__author__ = 'alex gao'

import threading

from grt.core import GRTMacro



class StraightSwerveMacro(GRTMacro):
    
    POWER = 1.0

    def __init__(self, swerve, timeout = None):
        super().__init__()
        self.swerve = swerve
        self.set_forward()
        self.enabled = False

    def macro_initialize(self):
        self.enable()
        threading.Timer(6, self.disable).start()

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False
        self.swerve.ackerman_turn(0, 0)
    def set_foward(self):
        self.swerve.ackerman_turn(0, self.POWER)

    def set_backwward(self):
        self.swerve.ackerman_turn(0, -self.POWER)







