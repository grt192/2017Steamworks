# import platform
# if "Linux" in platform.platform():
#     with open("/home/lvuser/py/grt/mechanism/camscript_new.py") as f:
#         code = compile(f.read(), "/home/lvuser/py/grt/mechanism/camscript_new.py", 'exec')
#         exec(code)

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
        self.t5 = config.shooter_m1

        # NEXT LINES CAUSE LAG ON ROBOT; ALSO WILL PROBABLY NOT WORK FOR 2017

        # self.camera = wpilib.USBCamera()
        # self.camera.setExposureManual(0.01) #.005
        # self.camera.setBrightness(80)
        # self.camera.setFPS(15)
        # self.camera_server = wpilib.CameraServer()
        # self.camera_server.startAutomaticCapture(self.camera)
        # self.camera_server.setQuality(10)


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
            # print("voltage")
            # print(self.t1.getOutputVoltage())
            #print("Encoder position:")
            # print(self.turn_motor.getEncPosition())
            # print(self.t1.getEncPosition())
            # print(self.t2.getEncPosition())
            # print(self.t3.getEncPosition())
            # print(self.t4.getEncPosition())
            # print(self.t4.getControlMode())
            print(self.t5.getEncPosition())


            
    def safeSleep(self, tinit, duration):
        tdif = .04 - (time.time() - tinit)
        if tdif > 0:
            time.sleep(tdif)
        if tdif <= 0:
            print("Code running slowly!")


if __name__ == "__main__":
    wpilib.run(MyRobot)
