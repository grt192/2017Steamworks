from wpilib import Talon
import math

class SwerveModule:
	
  	#8-motor drivetrain with 4 swerve modules
  	
    #power = 1


    def __init__(self, power_motor, turn_motor, power_encoder=None, turn_encoder=None, limit_switch):
        self.power_motor = power_motor
        self.turn_motor = turn_motor
        self.power_encoder = power_encoder
        self.turn_encoder = turn_encoder
        self.limit_switch = limit_switch
        

    


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

    def set_angle_1(self,angle):

        encoder_position = 



    def set_power(self, power, angle):
        pass

        #self.power_motor.set(power)

    def set_zero(self,power):

        if limit_switch.get()=0:

            self.turn_motor.set_angle(0)























