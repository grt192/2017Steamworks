from wpilib import Talon
import math

class SwerveModule:
	
  	#8-motor drivetrain with 4 swerve modules
  	
    #power = 1


    def __init__(self, power_motor, turn_motor, power_encoder=None, turn_encoder=None):
        self.power_motor = power_motor
        self.turn_motor = turn_motor
        self.power_encoder = power_encoder
        self.turn_encoder = turn_encoder
    


    def set_angle(self, angle):
		#angle*1024/2pi = self.turn_motor.getRaw()

        conversion = angle*1024/(2*math.pi)

        if(self.turn_motor.getPosition() % 1024 > 1024/2):



            encoder_position = self.turn_motor.getPosition() + (1024 - (self.turn_motor.getPosition() % 1024)) + conversion

            print("Going to:")
            print(encoder_position)

            #self.turn_motor.set(encoder_position)

        else:

            #reduction: 24 to 50

            encoder_position = self.turn_motor.getPosition() - (self.turn_motor.getPosition() % 1024) + conversion
            print("Going to:")
            print(encoder_position)

            self.turn_motor.set(encoder_position)



    def set_power(self, power):
        pass

        #self.power_motor.set(power)














