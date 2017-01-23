import wpilib
import time
import platform
#from grt.sensors.camera import CameraServer
#if "Linux" in platform.platform():
#    with open("/home/lvuser/py/grt/mechanism/camscript_new.py") as f:
#        code = compile(f.read(), "/home/lvuser/py/grt/mechanism/camscript_new.py", 'exec')
#        exec(code)


class MyRobot(wpilib.SampleRobot):
    def __init__(self):
        super().__init__()
        import config
        #self.sp = config.sp
        self.hid_sp = config.hid_sp
        self.ds = config.ds

        self.camera1 = wpilib.USBCamera()
        self.camera1.setExposureManual(0.005)
        self.camera1.setBrightness(80)
        self.camera1.setFPS(50)
        self.camera = wpilib.CameraServer()
        self.camera.startAutomaticCapture(self.camera1)
        self.camera.setQuality(50)
        #set quality from 1-100
        #self.camera.setSize(0)

        self.turn_motor = config.turn_motor


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
            # print("Encoder position:")
            # print(self.turn_motor.getEncPosition())
            
    def safeSleep(self, tinit, duration):
        tdif = .04 - (time.time() - tinit)
        if tdif > 0:
            time.sleep(tdif)
        if tdif <= 0:
            print("Code running slowly!")


if __name__ == "__main__":
    wpilib.run(MyRobot)
