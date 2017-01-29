

import wpilib
import time

#from config import sp

class MyRobot(wpilib.SampleRobot):
    def __init__(self):
        super().__init__()
        import config
        #self.sp = config.sp
        self.hid_sp = config.hid_sp
        self.sp = config.sp
        self.ds = config.ds
        

        #self.turn_motor = config.turn_motor

        self.t1 = config.turn_right
        self.t2 = config.turn_left
        self.t3 = config.turn_r2
        self.t4 = config.turn_l2


    def disabled(self):
        while self.isDisabled():
            tinit = time.time()
            self.hid_sp.poll()
            self.sp.poll()
            self.safeSleep(tinit, .04)

            # print("Encoder position:")
            # print(self.t4.getEncPosition())
            # print(self.t4.getControlMode())
    
    def autonomous(self):
        # define auto here
        pass
    
    def operatorControl(self):
        while self.isOperatorControl() and self.isEnabled():
            tinit = time.time()
            
            self.hid_sp.poll()
            self.sp.poll()
            self.safeSleep(tinit, .04)
            print("voltage")
            print(self.t1.getOutputVoltage())
            #print("Encoder position:")
            # print(self.turn_motor.getEncPosition())
            # print(self.t1.getEncPosition())
            # print(self.t2.getEncPosition())
            # print(self.t3.getEncPosition())
            # print(self.t4.getEncPosition())
            # print(self.t4.getControlMode())


            
    def safeSleep(self, tinit, duration):
        tdif = .04 - (time.time() - tinit)
        if tdif > 0:
            time.sleep(tdif)
        if tdif <= 0:
            print("Code running slowly!")


if __name__ == "__main__":
    wpilib.run(MyRobot)
