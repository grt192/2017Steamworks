# import platform
# if "Linux" in platform.platform():
#     with open("/home/lvuser/py/grt/mechanism/camscript_new.py") as f:
#         code = compile(f.read(), "/home/lvuser/py/grt/mechanism/camscript_new.py", 'exec')
#         exec(code)

import wpilib
import time

from wpilib import SendableChooser, SmartDashboard

# from config import middle_gear
# from config import basic_auto
# from config import blue_shoot_auto
# from config import red_shoot_auto

#from config import sp

#auto = middle_gear
# auto = None
# auto_exists = True

class MyRobot(wpilib.SampleRobot):
    def __init__(self):
        super().__init__()
        import config
        #self.sp = config.sp
        self.hid_sp = config.hid_sp
        self.sp = config.sp
        self.ds = config.ds

        self.middle_gear = config.middle_gear
        self.basic_auto = config.basic_auto
        self.blue_shoot_auto = config.blue_shoot_auto
        self.red_shoot_auto = config.red_shoot_auto

        # global auto
        # global auto_exists



        #auto = self.red_shoot_auto

        self.autoChooser = SendableChooser()
        self.autoChooser.addObject("No Autonomous", None)
        self.autoChooser.addObject("Red Shoot Auto", self.red_shoot_auto)
        #self.autoChooser.addObject("Cross And Shoot Auto", self.cross_and_shoot_auto)
        #self.autoChooser.addObject("Basic Auto", self.basic_auto)
        self.autoChooser.addDefault("Basic Auto", self.basic_auto)
        self.autoChooser.addObject("Blue Shoot Auto" , self.blue_shoot_auto)
        SmartDashboard.putData("Autonomous Mode", self.autoChooser)
        self.auto = self.autoChooser.getSelected()

        #wpilib.CameraServer.launch()
        wpilib.CameraServer.launch('vision.py:main')
        #ßßßwpilib.CameraServer.launch()
        #a = True
        #while a:
            #print("HIII")



        if self.auto == None:
            self.auto_exists = False
        else:
            self.auto_exists = True


        #self.turn_motor = config.turn_motor

        # self.t1 = config.turn_right
        # self.t2 = config.turn_left
        # self.t3 = config.turn_r2
        # self.t4 = config.turn_l2

        # self.lr1 = config.limit_r1
        # self.lr2 = config.limit_r2
        # self.ll1 = config.limit_l1
        # self.ll2 = config.limit_l2

        # self.s1 = config.shooter1_m1
        # self.s2 = config.shooter1_m2

        

        #wpilib.CameraServer.launch()

      

        # NEXT LINES CAUSE LAG ON ROBOT; ALSO WILL PROBABLY NOT WORK FOR 2017

        # self.camera = wpilib.USBCamera()
        # self.camera.setExposureManual(0.01) #.005
        # self.camera.setBrightness(80)
        # self.camera.setFPS(15)
        # self.camera_server = wpilib.CameraServer()
        # self.camera_server.startAutomaticCapture(self.camera)
        # self.camera_server.setQuality(10)


    def disabled(self):
        if self.auto_exists:
            self.auto.stop_autonomous()
        while self.isDisabled():
            #print("DISABLED")
            tinit = time.time()
            self.hid_sp.poll()
            self.sp.poll()
            self.safeSleep(tinit, .04)

            #print(self.ll2.pressed)

            # print("FRONT RIGHT L")
            # print(self.lr1.pressed)
            # print("BACK RIGHT L")
            # print(self.lr2.pressed)
            # print("FRONT LEFT L")
            # print(self.ll1.pressed)
            # print("BACK LEFT L")
            # print(self.ll2.pressed)
            

            # print("Encoder position:")
            # print(self.t4.getEncPosition())
            # print(self.t4.getControlMode())

            # print("SHOOTER 1")
            # print(self.s1.get())
            # print("SHOOTER 2")
            # print(self.s2.get())
    
    def autonomous(self):
        self.auto = self.autoChooser.getSelected()

        if self.auto == None:
            print("disabling auto")
            self.auto_exists = False

        else:
            self.auto_exists = True

        # define auto here

        #pass

        # print("IN THE AUTO FUNCTION")
        # print("IN THE AUTO FUNCTION")
        # print("IN THE AUTO FUNCTION")
        # print("IN THE AUTO FUNCTION")
        if self.auto_exists:
            #print("doing autonomous")

            self.auto.run_autonomous()
            while self.isAutonomous() and self.isEnabled():
                tinit = time.time()
                self.hid_sp.poll()
                self.sp.poll()
                self.safeSleep(tinit, .04)
            self.auto.stop_autonomous()
            print("done")
        else:
            pass

        # print("starting autonomous")
        # auto.run_autonomous()

        # while self.isAutonomous() and self.isEnabled():
        #     print("running autonomous")
        #     tinit = time.time()
        #     self.hid_sp.poll()
        #     self.sp.poll()
        #     #wpilib.Wait(0.04 - (time.time() - tinit))
        #     self.safeSleep(tinit, .04)

        # print("stopped autonomous")
        # auto.stop_autonomous()

    
    def operatorControl(self):
        if self.auto_exists:
            self.auto.stop_autonomous
        while self.isOperatorControl() and self.isEnabled():
            tinit = time.time()
            #print("ENABLEEED")
            
            self.hid_sp.poll()
            self.sp.poll()
            self.safeSleep(tinit, .04)

            # print("shooter speed:")
            # print(self.s1.get())
            #print(self.s2.get())
            # print("voltage")
            # print(self.t1.getOutputVoltage())
            #print("Encoder position:")
            # print(self.turn_motor.getEncPosition())
            # print(self.t1.getEncPosition())
            # print(self.t2.getEncPosition())
            # print(self.t3.getEncPosition())
            # print(self.t4.getEncPosition())
            #print(self.t4.getControlMode())

            # print(self.ll2.pressed)
            # print(self.t4.getEncPosition())

            # print("FRONT RIGHT L")
            # print(self.lr1.pressed)
            # print("BACK RIGHT L")
            # print(self.lr2.pressed)
            # print("FRONT LEFT L")
            # print(self.ll1.pressed)
            # print("BACK LEFT L")
            # print(self.ll2.pressed)
            # print("SHOOTER 1")
            # print(self.s1.get())
            # print(self.s1.getClosedLoopError())
            # print("SHOOTER 2")
            # print(self.s2.get())
            # print(self.s2.getClosedLoopError())
            # print("SHOOTER 2")
            # print(self.s2.get())



            
    def safeSleep(self, tinit, duration):
        tdif = .04 - (time.time() - tinit)
        if tdif > 0:
            time.sleep(tdif)
        if tdif <= 0:
            print("Code running slowly!")


if __name__ == "__main__":
    wpilib.run(MyRobot)

