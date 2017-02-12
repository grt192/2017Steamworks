class Camera:
	def run():
		self.camera1 = wpilib.USBCamera()
    	self.camera1.setExposureManual(0.005)
    	self.camera1.setBrightness(80)
    	self.camera1.setFPS(50)
    	self.camera = wpilib.CameraServer()
    	self.camera.startAutomaticCapture(self.camera1)
    	self.camera.setQuality(50)