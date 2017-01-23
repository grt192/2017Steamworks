from wpilib import Talon
import math

class SwerveModule:
	
  	#8-motor drivetrain with 4 swerve modules


    def __init__(self, turn_r1, turn_r2, turn_l1, turn_l2, power_r1, power_r2, power_l1, power_l2, limit_r1=None, limit_r2=None, limit_l1=None, limit_l2=None):
        
        self.turn_r1 = turn_r1
        self.turn_r2 = turn_r2
        self.turn_l1 = turn_l1
        self.turn_l2 = turn_l2

        self.power_r1 = power_r1
        self.power_r2 = power_r2
        self.power_l1 = power_l1
        self.power_l2 = power_l2

        self.limit_r1 = limit_r1
        self.limit_r2 = limit_r2
        self.limit_l1 = limit_l1
        self.limit_l2 = limit_l2

        limit_r1.add_listener(self._limit_listener)
        limit_r2.add_listener(self._limit_listener)
        limit_l1.add_listener(self._limit_listener)
        limit_l2.add_listener(self._limit_listener)

        self.HEIGHT = 24
        self.WIDTH = 16

        #MAX ANGLE FOR OUTSIDE WHEEL
        self.theta_1 = math.atan2(self.HEIGHT, self.WIDTH)

        #MAX ANGLE FOR INSIDE WHEEL
        self.theta_2 = math.pi - self.theta_1

        self.TICKS_PER_REV = 4096*50/24 #I THINK SO!

        self.strafing = False

    def ackerman_turn(self, joy_angle, power):

        if joy_angle >= 0:

            #QUADRANT 1

            if joy_angle <= math.pi/2:

            #CONVERTS FROM JOYSTICK ANGLE IN A 90 DEGREE RANGE TO THE RANGE OF THE TWO MAXES

            outer_angle = self.theta_1 * joy_angle / (math.pi/2)
            inner_angle = self.theta_2 * joy_angle / (math.pi/2)

        elif joy_angle == math.pi:
            outer_angle = 0
            inner_angle = 0

        #QUADRANT 4

        else:
            
            #The goal here is to have the wheel go to an angle within -90 to +90 but go backwards. 
            #We mod 90 in order to make the same conversion that we did in Q1.
            #Then you subtract 90 to make it go to the opposite quadrant.

            #EXAMPLE CASE:
            # Our joystick reads 175. Mod 90 that's 85. Then subtract 90 and you get -5. 
            # -5 and 175 are along the same line, so by going backwards from here we go the same direction
            # as 175. 

            outer_angle = self.theta_1 * (-(math.pi/2) + (joy_angle % (math.pi/2)))/(math.pi/2)
            inner_angle = self.theta_2 * (-(math.pi/2) + (joy_angle % (math.pi/2)))/(math.pi/2)


    else:

        #QUADRANT 2

        if joy_angle >= -math.pi/2:

            #Same exact thing as Q1

            outer_angle = self.theta_1 * joy_angle / (math.pi/2)
            inner_angle = self.theta_2 * joy_angle / (math.pi/2)

        elif joy_angle == -math.pi:
            outer_angle = 0
            inner_angle = 0

        #QUADRANT 3

        else:
            
            #Almost the same as Q4. You mod -90 since the angle will be negative. 
            #You add 90 instead of subtracting for the same reason.

            outer_angle = self.theta_1 * ((math.pi/2) + (joy_angle % (-math.pi/2)))/(math.pi/2)
            inner_angle = self.theta_2 * ((math.pi/2) + (joy_angle % (-math.pi/2)))/(math.pi/2)



    outer_speed = power

    #avoids divison by 0
    if inner_angle == 0:
        inner_speed = power

    #Decreases the inner speed by the appropriate amount.
    else:
        inner_speed = power * math.sin(outer_angle)/math.sin(inner_angle)


    #Conversion from radians to encoder ticks
    outer_pos = outer_angle*self.TICKS_PER_REV/(2*math.pi)
    inner_pos = inner_angle*self.TICKS_PER_REV/(2*math.pi)

   

    if abs(joy_angle) < math.pi/2: #is in quadrant 1 or 2

        if joy_angle <= 0: #is in quadrant 2

            #In quadrant 2 you turn left, so right is outer and left is inner. 
            #Back wheels are reversed for position for super tight turning.

            self.turn_r1.set(outer_pos)
            self.turn_r2.set(-outer_pos)
            self.turn_l1.set(inner_pos)
            self.turn_l2.set(-inner_pos)

            self.power_r1.set(outer_speed)
            self.power_r2.set(outer_speed)
            self.power_l1.set(inner_speed)
            self.power_l2.set(inner_speed)
            

        else: # is in quadrant 1

            #Same as Q2 but turn right.

            self.turn_l1.set(outer_pos)
            self.turn_l2.set(-outer_pos)
            self.turn_r1.set(inner_pos)
            self.turn_r2.set(-inner_pos)

            self.power_l1.set(outer_speed)
            self.power_l2.set(outer_speed)
            self.power_r1.set(inner_speed)
            self.power_r2.set(inner_speed)
            #print("done2")

    #same as above but goes backwards
    else: # is in quadrant 3 or 4


        if joy_angle >= 0: # is in quadrant 4
        
            self.turn_r1.set(outer_pos)
            self.turn_r2.set(-outer_pos)
            self.turn_l1.set(inner_pos)
            self.turn_l2.set(-inner_pos)

            self.power_r1.set(-outer_speed)
            self.power_r2.set(-outer_speed)
            self.power_l1.set(-inner_speed)
            self.power_l2.set(-inner_speed)
            #print("done3")

        else: # is in quadrant 3 


            self.turn_r1.set(inner_pos)
            self.turn_r2.set(-inner_pos)
            self.turn_l1.set(outer_pos)
            self.turn_l2.set(-outer_pos)

            self.power_r1.set(-inner_speed)
            self.power_r2.set(-inner_speed)
            self.power_l1.set(-outer_speed)
            self.power_l2.set(-outer_speed)


    def strafe(self, joy_angle, power):

        position = joy_angle * self.TICKS_PER_REV / (2*math.pi)
               

        #USES MOTOR TURN_R1 TO DETERMIN THE CURRENT POSITION.
        #Not sure if it would be better to do this individually for each motor.

        cur_angle = self.turn_r1.getEncPosition()*(2*math.pi)/self.TICKS_PER_REV

        #IF THE WHEEL IS CURRENTLY IN Q3 OR Q4 AND NEEDS TO GO TO THE OTHER ONE

        if (abs(cur_angle) > math.pi/2) and (abs(position) > (self.TICKS_PER_REV/4)) and (cur_angle * position < 0): 


            #IF IN Q4 SET CURRENT POSITION TO CURRENT POSITION - 2*PI

            if cur_angle > 0:
                print(cur_angle - 2*math.pi)
                self.turn_r1.setEncPosition(cur_angle * self.TICKS_PER_REV / (2*math.pi) - self.TICKS_PER_REV)
                self.turn_r2.setEncPosition(cur_angle * self.TICKS_PER_REV / (2*math.pi) - self.TICKS_PER_REV)
                self.turn_l1.setEncPosition(cur_angle * self.TICKS_PER_REV / (2*math.pi) - self.TICKS_PER_REV)
                self.turn_l2.setEncPosition(cur_angle * self.TICKS_PER_REV / (2*math.pi) - self.TICKS_PER_REV)
            
            #IF IN Q3 SET CURRENT POSITION TO CURRENT POSITION + 2*PI

            else: 
                print(cur_angle + 2*math.pi)
                self.turn_r1.setEncPosition(cur_angle * self.TICKS_PER_REV / (2*math.pi) + self.TICKS_PER_REV)
                self.turn_r2.setEncPosition(cur_angle * self.TICKS_PER_REV / (2*math.pi) + self.TICKS_PER_REV)
                self.turn_l1.setEncPosition(cur_angle * self.TICKS_PER_REV / (2*math.pi) + self.TICKS_PER_REV)
                self.turn_l2.setEncPosition(cur_angle * self.TICKS_PER_REV / (2*math.pi) + self.TICKS_PER_REV)


        
        self.turn_r1.set(position)
        self.turn_r2.set(position)
        self.turn_l1.set(position)
        self.turn_l2.set(position)

        self.power_r1.set(power*.25)
        self.power_r2.set(power*.25)
        self.power_l1.set(power*.25)
        self.power_l2.set(power*.25)


    def set_strafing(self, boolean):
        self.strafing = boolean


    def _limit_listener(self, source, state_id, datum):

        if state_id == 'pressed' and datum and self.strafing:

            if source == self.limit_r1:

                self.turn_r1.setEncPosition(0)

            if source == self.limit_r2:

                self.turn_r2.setEncPosition(0)

            if source == self.limit_l1:
                self.turn_l1.setEncPosition(0)

            if source == self.limit_l2:
                self.turn_l2.setEncPosition(0)









