from grt.core import GRTMacro
import wpilib
import threading
import math

#constants = Constants()


class StraightStrafeMacro(GRTMacro):
    """
    Drive Macro; drives forwards a certain distance while
    maintaining orientation
    """

    DT_NO_TARGET_TURN_RATE = .2
    DT_KP = .03
    DT_KI = 0
    DT_KD = 0
    DT_ABS_TOL = 5
    DT_OUTPUT_RANGE = .25
    POWER = .4

    def __init__(self, swevre, navx, angle, timeout=None):
        """
        Pass drivetrain, distance to travel (ft), and timeout (secs)
        """
        super().__init__(timeout)
        self.set_forward()
        self.operation_manager = None
        self.swerve = swerve
        self.enabled = False
        self.navx = navx

        self.setpoint = None

        self.angle = angle

        self.pid_controller = wpilib.PIDController(self.DT_KP, self.DT_KI,
                                                   self.DT_KD, self.get_input,
                                                   self.set_output)
        self.pid_controller.setAbsoluteTolerance(self.DT_ABS_TOL)
        self.pid_controller.reset()

        self.pid_controller.setInputRange(0.0,  360.0)
        self.pid_controller.setContinuous(True)


        self.pid_controller.setOutputRange(-.4, .4)
        #self.run_threaded()

    def macro_initialize(self):
        self.enable()
        threading.Timer(6, self.disable).start()

    def macro_stop(self):
        self.disable()

    def set_forward(self):
        #Negative value is forward, positive value is reverse
        if self.POWER > 0:
            self.POWER *= -1

    def set_reverse(self):
        if self.POWER < 0:
            self.POWER *= -1


    def enable(self):
        self.setpoint = self.navx.fused_heading
        offset = self.angle * 180/math.pi
        self.pid_controller.setSetpoint(self.setpoint + offset)
        self.pid_controller.enable()
        self.enabled = True

    def disable(self):
        self.pid_controller.disable()
        self.setpoint = None
        self.enabled = False
        self.swerve.set_power(0)
        if not self.operation_manager == None:
            self.operation_manager.op_lock = False
        #self.terminate()

    def set_output(self, output):
        """
        :param output: (-.5, .5)
        :return:
        """
        if self.enabled:
            if not self.pid_controller.onTarget():
                self.swerve.strafe(self.angle + output, self.POWER, .4)
                #self.dt.set_dt_output((self.POWER+.06) + output, self.POWER -output)
            else:
                self.swerve.strafe(self.angle, self.POWER, .4)
                #self.dt.set_dt_output(self.POWER+.06, self.POWER)
            print("Setpoint: ", self.pid_controller.getSetpoint())
            print("Output: ", output)

    def get_input(self):
        print("Input: ", self.navx.fused_heading)
        return self.navx.fused_heading