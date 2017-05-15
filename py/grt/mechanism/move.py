from ctre import CANTalon

class Move:

	def __init__(self, motor):
		self.motor = motor

	def increment(self, power):
		power += .1
		self.motor.set(power)
		print(power)