

import wpilib
import time


class MyRobot(wpilib.SampleRobot):
    def __init__(self):
        super().__init__()
        import config
        #self.sp = config.sp
        self.hid_sp = config.hid_sp
        self.ds = config.ds
        self.limit_switch = config.limit_switch

        self.turn_2 = config.turn_2


    def disabled(self):
        while self.isDisabled():
            tinit = time.time()
            self.hid_sp.poll()
            self.safeSleep(tinit, .04)
    
    def autonomous(self):
        # define auto here
        pass
    
    def operatorControl(self):
        while self.isOperatorControl() and self.isEnabled():
            tinit = time.time()
            #self.sp.poll()
            self.hid_sp.poll()
            self.safeSleep(tinit, .04)
            print(self.limit_switch.get())
            print(self.turn_2.getEncPosition())
            if self.limit_switch.get():
                    self.turn_2.setEncPosition(0)
                    #print("triggered")
            
    def safeSleep(self, tinit, duration):
        tdif = .04 - (time.time() - tinit)
        if tdif > 0:
            time.sleep(tdif)
        if tdif <= 0:
            print("Code running slowly!")


if __name__ == "__main__":
    wpilib.run(MyRobot)
