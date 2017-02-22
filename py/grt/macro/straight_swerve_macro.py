
__author__ = 'alex gao'

import threading
from grt.core import GRTMacro
import time

class StraightSwerveMacro(GRTMacro):

    POWER = 0.5

    def __init__(self, swerve, timeout=None):
        super().__init__()
        self.swerve = swerve
        #self.enabled = False

        #self.abort = False


    def abort(self):
        self.abort = True

    def initialize(self):
        print("initialized")
        #self.enable()
        self.rotate()
        print("straight swerve enabled")
        threading.Timer(6, self.disable).start()

     # def enable(self):
     #    print("Running portcullis_macro")
     #    self.abort = False
     #    self.pickup.go_to_pickup_position()
     #    self._angle_change_with_abort()
     #    angle_change_timer = threading.Timer(1, self.disable)
     #    print("running achange timer")
     #    angle_change_timer.start()
     #    print("finished achange timer")


     #    while self.running_angle_change:
     #        pass

     #    self.straight_macro.set_forward()
     #    self.straight_macro.enable()
     #    straight_macro_timer = threading.Timer(2, self.straight_macro.disable)
     #    straight_macro_timer.start()

    def enable(self):
        self.enabled = True
        #print("RUNNING EASY AUTO")
        #self.abort = False
        #self.swerve.strafe(0,1,.5)
        #strafe_timer = threading.Timer(2, self.disable)
        #print("running timer")
        #strafe_timer.start()
        #self.swerve.strafe(0,0,0)


    def disable(self):
        #self.swerve.ackerman_turn(0, 0)
        self.swerve.strafe(0, 0, 1)
        print("straight swerve disabled")
        #self.abort()
        #self.enabled = False
        
    def die(self):
        self.disable()
        

    def rotate(self):
        print("rotating")
        self.swerve.strafe(math.pi/2, self.POWER, 1)

    def set_forward(self):
        self.swerve.ackerman_turn(0, self.POWER)

    def set_backward(self):
        self.swerve.ackerman_turn(0, -self.POWER)

    

# class RockingChairMacro(GRTMacro):

#     def __init__(self, rocking_chair, timeout=None):
#         super().__init__(timeout=timeout)
#         self.rocking_chair = rocking_chair
#         self.enabled = False

#     def macro_periodic(self):
#         if self.enabled:
#             self.rocking_chair.set_motor(.7)
#             time.sleep(1)
#             self.rocking_chair.set_motor(0)
#             time.sleep(.1)
#             self.rocking_chair.set_motor(-.7)
#             time.sleep(1)
#             self.rocking_chair.set_motor(0)
#             time.sleep(.1)

#     def macro_stop(self):
#         self.rocking_chair.set_motor(0)
#         self.enabled = False