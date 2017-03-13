from grt.core import GRTMacro
import wpilib
import threading
import math

class RotateMacro(GRTMacro):

	def __init__(self, swerve, scale, timeout=None):
		super().__init__(timeout=timeout)
		self.swerve = swerve
		self.scale = scale
		self.enabled = False

	def macro_periodic(self):
		if self.enabled:
			print("macro enabled")
			print("macro enabled")
			print("macro enabled")
			
			self.swerve.ackerman_turn(math.pi/2, 1, self.scale)

	def macro_stop(self):
		self.swerve.set_power(0)
		self.enabled = False