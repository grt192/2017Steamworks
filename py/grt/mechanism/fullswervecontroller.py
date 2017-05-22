import math
from ctre import CANTalon
from collections import OrderedDict

class FullSwerveController:

	def __init__(self, joystick, xbox_controller, full_swerve_module):

		self.full_swerve_module = full_swerve_module

		self.joystick = joystick
		self.xbox_controller = xbox_controller

		self.joystick.add_listener(self._joylistener)
		self.xbox_controller.add_listener(self._xbox_controller_listener)

	def _joylistener(self, sensor, state_id, datum):

		pass
			

	def _xbox_controller_listener(self, sensor, state_id, datum):

		#RIGHT JOYSTICK FOR STRAFING

		if state_id in ('r_y_axis', 'r_x_axis'):

			
			x = self.xbox_controller.r_x_axis
			y = self.xbox_controller.r_y_axis

			
			if abs(x) > .2 or abs(y) > .2:
				rot_angle = math.atan2(x, -y)


		if state_id in ('l_y_axis', 'l_x_axis'):

			x = self.xbox_controller.l_x_axis
			y = self.xbox_controller.l_y_axis

			if (abs(x) > .2 or abs(y) > .2):

				joy_angle = math.atan2(x, -y)

				#DETERMINE POWER: size of vector based on joystick x and y

				joy_vector = (math.sqrt(x**2 + y**2))/(math.sqrt(2))

		if state_id == 'button1':
			print("Working")
				
		self.full_swerve_module.full_swerve(joy_angle, joy_vector, rot_angle)


				

