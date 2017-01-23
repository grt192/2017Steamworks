class Camera:

    def cameraTest():
        self.camera = wpilib.USBCamera()
        self.camera.startCapture()
        self.camServ = wpilib.CameraServer()
        self.camServ.startAutomaticCapture(self.camera)
        print("test")
        except:
            self.camera = None
