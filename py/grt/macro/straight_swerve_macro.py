__author__ = 'alex gao'

import threading
from grt.core import GRTMacro
import time
import wpilib
import math

class StraightSwerveMacro(GRTMacro):

    KP =  .03#.03
    KI = 0
    KD = 1
    ABS_TOL = .05  #need to test
    POWER = 0.3

    def __init__(self, swerve, navx=None, timeout=None):
        super().__init__()
        self.swerve = swerve
        self.enabled = False
        self.setpoint = None

        self.navx = navx

        self.pid_controller = wpilib.PIDController(self.KP, self.KI,
                                                   self.KD, self.get_input,
                                                   self.set_output)

        # max tolerance for use with OnTarget
        self.pid_controller.setAbsoluteTolerance(self.ABS_TOL) 
        self.pid_controller.reset()

        self.pid_controller.setInputRange(0.0,  360.0)
        self.pid_controller.setContinuous(True)

        self.pid_controller.setOutputRange(-math.pi, math.pi)
    

    # def abort(self):
    #     self.abort = True

    def initialize(self):

        self.swerve.strafe(math.pi/2, 0, 1)

        time.sleep(1)
        print("straight swerve enabled")
        self.swerve.sideways_ackerman_turn(0.1, self.POWER)
        #self.enable()
        time.sleep(4.20)
        
        self.kill()
        self.die()

        

        #threading.Timer(1, self.disable).start()

    def enable(self):
        

        #self.swerve.ackerman_turn(0, self.POWER)
        self.swerve.sideways_ackerman_turn(0,self.POWER)
        #time.sleep(.5)
        # self.swerve.sideways_ackerman_turn(.1,self.POWER)
        # time.sleep(2)

        #self.swerve.strafe(math.pi/2, self.POWER,  1)
        self.setpoint = self.navx.fused_heading
        self.pid_controller.setSetpoint(self.setpoint)
        self.pid_controller.enable()
        self.enabled = True


    def disable(self):
        self.swerve.set_power(0)
        print("straight swerve disabled")
        self.pid_controller.disable()
        self.setpoint = None
        self.enabled = False
        
    def die(self):
        self.disable()
        
    def set_forward(self):
        self.swerve.ackerman_turn(0, self.POWER)

    # def set_backward(self):
    #     self.swerve.ackerman_turn(0, -self.POWER)

    def set_output(self, output):
        if self.enabled:
            if not self.pid_controller.onTarget():
                # Need to test correction/output
                #self.swerve.strafe(math.pi/2 + output, self.POWER, 1) <-- TRY THIS ONE TOO
                #self.swerve.ackerman_turn(output, self.POWER)
                self.swerve.sideways_ackerman_turn(output, self.POWER)
            else:
                #self.swerve.ackerman_turn(0, self.POWER)
                self.swerve.sideways_ackerman_turn(0, self.POWER)

            print("Position: ", self.navx.fused_heading)
            print("Setpoint: ", self.pid_controller.getSetpoint())
            print("Output: ", output)


    def get_input(self):
        return self.navx.fused_heading
