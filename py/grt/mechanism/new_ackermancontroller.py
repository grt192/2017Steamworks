import math
from ctre import CANTalon
from collections import OrderedDict

from grt.macro.rotate_macro import RotateMacro

class NewAckermanController:

	def __init__(self, joystick, xbox_controller, swerve_module, record_macro=None, playback_macro=None):

		self.swerve_module = swerve_module

		self.joystick = joystick
		self.xbox_controller = xbox_controller

		self.record_macro = record_macro
		self.playback_macro = playback_macro

		self.ackerman_power = .7
		self.strafe_power = 1

		self.rotate_macro_forward = RotateMacro(self.swerve_module, self.ackerman_power)
		self.rotate_macro_forward.run_threaded()
		self.rotate_macro_backward = RotateMacro(self.swerve_module, (-1)*self.ackerman_power)
		self.rotate_macro_backward.run_threaded()

		self.instructions = OrderedDict([("1, <class 'wpilib.cantalon.CANTalon'>", [-0.01857282502443793, -0.01857282502443793, -0.01857282502443793, 0.01857282502443793, 0.05571847507331378, 0.01857282502443793, -0.04398826979472141, -0.011730205278592375, 0.06842619745845552, 0.11241446725317693, 0.1935483870967742, 0.1935483870967742, 0.21212121212121213, 0.22482893450635386, 0.22482893450635386, 0.22482893450635386, 0.22482893450635386, 0.1436950146627566, -0.03714565004887586, 0.011730205278592375]), ("7, <class 'wpilib.cantalon.CANTalon'>", [-0.03128054740957967, -0.03128054740957967, -0.03128054740957967, 0.01857282502443793, -0.030303030303030304, 0.01857282502443793, -0.04398826979472141, 0.011730205278592375, -0.06842619745845552, -0.15640273704789834, -0.1935483870967742, -0.1935483870967742, -0.22482893450635386, -0.22482893450635386, -0.22482893450635386, -0.22482893450635386, -0.22482893450635386, -0.18084066471163246, -0.04985337243401759, 0.0]), ("100, <class 'grt.macro.assistance_macros.ElevatorMacro'>", [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), ("5, <class 'wpilib.cantalon.CANTalon'>", [0.0, 0.0, 0.0, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, 0.0, 0.0, 0.0])])

		

		self.joystick.add_listener(self._joylistener)
		self.xbox_controller.add_listener(self._xbox_controller_listener)

	def _joylistener(self, sensor, state_id, datum):

		pass

		# if state_id in ('y_axis', 'x_axis'):

		#     x = self.joystick.x_axis
		#     y = self.joystick.y_axis

		#     if self.swerve_module.get_strafing():

		  
		#         if abs(x) > .05 or abs(y) > .05:

					

		#             angle = math.atan2(x,-y)
					

		#             power = math.sqrt(x ** 2 + y ** 2)

		#             self.swerve_module.strafe(angle, power, .6)

		#         else:

		#             self.swerve_module.set_power(0)

		#     else:

		#         if (abs(x) > .05 or abs(y) > .05):

		#             joy_angle = math.atan2(x, -y)
		#             print("JOY ANGLE")
		#             print(joy_angle)

		#             #DETERMINE POWER: size of vector based on joystick x and y

		#             power = math.sqrt(x**2 + y**2)
					
		#             self.swerve_module.ackerman_turn(joy_angle, power)


		#         else:

		#             self.swerve_module.set_power(0)


		# if state_id == 'trigger':

		#     if datum:
		#         print("SWITCHED TO STRAFING")
		#         self.swerve_module.set_strafing(True)

		#     else:
		#         print("SWITCHED TO ACKERMAN")
		#         self.swerve_module.set_strafing(False)

		# if state_id == 'button8':

		#     if datum:
		#         self.swerve_module.zero(.35)

		# if state_id == 'button9':

		#     if datum:
		#         self.swerve_module.zero(.5)

		# if state_id == 'button4':

		#     if datum:

		#         self.swerve_module.switch_to_percentvbus()


		# if state_id == 'button5':

		#     if datum:

		#         self.swerve_module.set_enc_position(0)
			

	def _xbox_controller_listener(self, sensor, state_id, datum):

		#TO ZERO: press B, move to correct positions, then press A

		# if state_id == 'a_button':

		#     if datum:

		#         self.swerve_module.set_enc_position(0)

		# if state_id == 'b_button':

		#     if datum: 

		#         self.swerve_module.switch_to_percentvbus()

		# #MANUAL SWITCH TO STRAFING

		# if state_id == 'x_button':

		#     if datum:

		#         self.swerve_module.set_strafing(True)
		#         print("SWITCHED TO STRAFING")

		# #MANUAL SWITCH TO ACKERMAN

		# if state_id == 'y_button':

		#     if datum:

		#         self.swerve_module.set_strafing(False)
		#         print("SWITCHED TO ACKERMAN")

		if state_id == 'a_button':

			if datum:
				self.swerve_module.zero(.25)

		if state_id == 'b_button':

			if datum:
				self.swerve_module.zero(.4)

		# if state_id == "a_button":
		# 	if datum:
		# 		print("Recording started")
		# 		self.record_macro.start_record()
		# if state_id == "b_button":
		# 	if datum:
		# 		print("Recording stopped")
		# 		self.record_macro.stop_record()
				#self.record_macro.instructions = self.instructions
		# if state_id == "x_button":
		# 	if datum:
		# 		self.playback_macro.load("/home/lvuser/py/instructions.py")
		# 		self.playback_macro.start_playback()#self.instructions)
		# if state_id == "y_button":
		# 	if datum:
		# 		self.playback_macro.stop_playback()

		if state_id == 'start_button':
			if datum:
				if self.strafe_power == 1:
					#print("switching strafe to slow")
					self.strafe_power = .4
				elif self.strafe_power == .4:
					#print("swithing strafe to fast")
					self.strafe_power = 1

		if state_id == 'back_button':
			if datum:
				if self.ackerman_power == .7:
					#print("switching ackerman to fast")
					self.ackerman_power = 1
				elif self.ackerman_power == 1:
					#print("switching ackerman to slow")
					self.ackerman_power = .7

		if state_id == 'r_shoulder': 
			if datum:
				#print("GOING")
				self.swerve_module.ackerman_turn(math.pi/2, 1, 0)
				self.rotate_macro_forward.enabled = True
				#self.swerve_module.ackerman_turn(math.pi/2, 1, self.ackerman_power)
			else:
				#print("STOPPING SWERVE")
				self.rotate_macro_forward.macro_stop()
				self.rotate_macro_forward.enabled = False
				#self.swerve_module.set_power(0)

		if state_id == 'l_shoulder':
			if datum:
				#print("GOING")
				self.swerve_module.ackerman_turn(math.pi/2, 1, 0)
				self.rotate_macro_backward.enabled = True
				#self.swerve_module.ackerman_turn(math.pi/2, 1, -self.ackerman_power)
			else:
				#print("STOPPING SWERVE")
				self.rotate_macro_backward.macro_stop()
				self.rotate_macro_backward.enabled = False
				#self.swerve_module.set_power(0)


		#RIGHT JOYSTICK FOR STRAFING

		if state_id in ('r_y_axis', 'r_x_axis'):

			
			x = self.xbox_controller.r_x_axis
			y = self.xbox_controller.r_y_axis

			
			if abs(x) > .2 or abs(y) > .2:

				self.swerve_module.set_strafing(True)
				#print("SWITCHED TO STRAFING")

				angle = math.atan2(x,-y)
				

				power = math.sqrt(x ** 2 + y ** 2)

				self.swerve_module.strafe(angle, power, self.strafe_power)

			else:

				self.swerve_module.set_power(0)

				self.swerve_module.set_strafing(False)
				#print("SWITCHED TO ACKERMAN")

		if state_id in ('l_y_axis', 'l_x_axis'):

			x = self.xbox_controller.l_x_axis
			y = self.xbox_controller.l_y_axis
			# print("x: ",x)
			# print("y: ",y)

			if (abs(x) > .2 or abs(y) > .2) and not self.swerve_module.get_strafing():

				joy_angle = math.atan2(x, -y)
				# print("JOY ANGLE")
				# print(joy_angle)

				#DETERMINE POWER: size of vector based on joystick x and y

				power = (math.sqrt(x**2 + y**2))/(math.sqrt(2))
				
				self.swerve_module.ackerman_turn(joy_angle, power, self.ackerman_power)


			else:

				self.swerve_module.set_power(0)
				

	# def _limit_listener(self, source, state_id, datum):

	#     if state_id == 'pressed' and datum and self.strafing:


	#         print("listener zeroing")

	#         self.turn_r1.setEncPosition(0)
	#         self.turn_r2.setEncPosition(0)
	#         self.turn_l1.setEncPosition(0)
	#         self.turn_l2.setEncPosition(0)