from ctre import CANTalon

class Shooter:

	def __init__(self, shooter1_m1, shooter1_m2, load_m, pneumatic, shooter2_m1=None, shooter2_m2=None):

		self.shooter1_m1 = shooter1_m1
		self.shooter1_m2 = shooter1_m2
		self.shooter2_m1 = shooter2_m1
		self.shooter2_m2 = shooter2_m2

		self.load_m = load_m

		self.pneumatic = pneumatic

	def ramp_up_speed(self, vel_1, vel_2):
		self.shooter1_m1.changeControlMode(CANTalon.ControlMode.Speed)
		self.shooter1_m1.setPID(1.0,0.008,40, f=0.47383)
		self.shooter1_m1.set(-vel_1)
		self.shooter1_m2.changeControlMode(CANTalon.ControlMode.Speed)
		self.shooter1_m2.setPID(1.5,0.008,50, f=0.478037)
		self.shooter1_m2.set(vel_2)

	def ramp_down_to_zero(self):
		self.shooter1_m1.changeControlMode(CANTalon.ControlMode.PercentVbus)
		self.shooter1_m1.set(0)
		self.shooter1_m2.changeControlMode(CANTalon.ControlMode.PercentVbus)
		self.shooter1_m2.set(0)

		

	def shoot(self):
		self.load_m.set(1)

	def stop(self):
		self.load_m.set(0)

	def angle_change_up(self):
		self.pneumatic.set(.8)

	def angle_change_down(self):
		self.pneumatic.set(0)

class Intake:

	def __init__(self, motor):

		self.motor = motor

	def intake(self):
		print("intaking from intake")
		self.motor.set(1)

	def stop(self):
		self.motor.set(0)

class Climber:

	def __init__(self, motor):
		
		self.motor = motor

	def climb(self):
		self.motor.set(-1)

	def down(self):
		self.motor.set(1)

	def stop(self):
		self.motor.set(0)

	def climb_adjustable(self, power):
		self.motor.set(power)

class Gear:

	def __init__(self, pneumatic_1, pneumatic_2):

		self.pneumatic_1 = pneumatic_1
		self.pneumatic_2 = pneumatic_2

	def place(self):
		self.pneumatic_1.set(1)

	def retract(self):
		self.pneumatic_1.set(0)

	def unjam_up(self):
		self.pneumatic_2.set(1)

	def unjam_down(self):
		self.pneumatic_2.set(0)

class Hopper:

	def __init__(self, pneumatic):

		self.pneumatic = pneumatic

	def unjam_out(self):
		self.pneumatic.set(1)

	def unjam_in(self):
		self.pneumatic.set(0)

