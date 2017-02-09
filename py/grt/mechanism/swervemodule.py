from ctre import CANTalon
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

        self.zeroing = [False, False, False, False]

    def ackerman_turn(self, joy_angle, power):

        real = [0,0,0,0]

        turn_motors = (self.turn_r1, self.turn_r2, self.turn_l1, self.turn_l2)
        

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

                

                for i in range(4):

                    real[i] = (turn_motors[i].getEncPosition() * ((2*math.pi)/self.TICKS_PER_REV)) % (2*math.pi) 

                    if real[i] > math.pi:

                        real[i] -= 2*math.pi

                adjustment_factors = [0,0,0,0]

                adjustment_factors[0] = outer_angle - real[0]
                adjustment_factors[1] = -outer_angle - real[1]
                adjustment_factors[2] = inner_angle - real[2]
                adjustment_factors[3] = -inner_angle - real[3]

                positions = [0,0,0,0]

                for i in range(4):

                    positions[i] = turn_motors[i].getEncPosition() + adjustment_factors[i] * self.TICKS_PER_REV/(2*math.pi)

                    turn_motors[i].set(positions[i])

                # self.turn_r1.set(outer_pos)
                # self.turn_r2.set(-outer_pos)
                # self.turn_l1.set(inner_pos)
                # self.turn_l2.set(-inner_pos)

                self.power_r1.set(outer_speed)
                self.power_r2.set(outer_speed)
                self.power_l1.set(inner_speed)
                self.power_l2.set(inner_speed)
                

            else: # is in quadrant 1

                #Same as Q2 but turn right.

                

                for i in range(4):

                    real[i] = (turn_motors[i].getEncPosition() * ((2*math.pi)/self.TICKS_PER_REV)) % (2*math.pi) 

                    if real[i] > math.pi:

                        real[i] -= 2*math.pi

                adjustment_factors = [0,0,0,0]

                adjustment_factors[0] = inner_angle - real[0]
                adjustment_factors[1] = -inner_angle - real[1]
                adjustment_factors[2] = outer_angle - real[2]
                adjustment_factors[3] = -outer_angle - real[3]

                positions = [0,0,0,0]

                for i in range(4):

                    positions[i] = turn_motors[i].getEncPosition() + adjustment_factors[i] * self.TICKS_PER_REV/(2*math.pi)

                    turn_motors[i].set(positions[i])

                # self.turn_l1.set(outer_pos)
                # self.turn_l2.set(-outer_pos)
                # self.turn_r1.set(inner_pos)
                # self.turn_r2.set(-inner_pos)

                self.power_l1.set(outer_speed)
                self.power_l2.set(outer_speed)
                self.power_r1.set(inner_speed)
                self.power_r2.set(inner_speed)
                #print("done2")

        #same as above but goes backwards
        else: # is in quadrant 3 or 4


            if joy_angle >= 0: # is in quadrant 4


                

                for i in range(4):

                    real[i] = (turn_motors[i].getEncPosition() * ((2*math.pi)/self.TICKS_PER_REV)) % (2*math.pi) 

                    if real[i] > math.pi:

                        real[i] -= 2*math.pi

                adjustment_factors = [0,0,0,0]

                adjustment_factors[0] = outer_angle - real[0]
                adjustment_factors[1] = -outer_angle - real[1]
                adjustment_factors[2] = inner_angle - real[2]
                adjustment_factors[3] = -inner_angle - real[3]

                positions = [0,0,0,0]

                for i in range(4):

                    positions[i] = turn_motors[i].getEncPosition() + adjustment_factors[i] * self.TICKS_PER_REV/(2*math.pi)

                    turn_motors[i].set(positions[i])

                # print("QUADRANT 4 OUTER POS")
                # print(outer_pos)
                # print("QUADRANT 4 INNER POS")
                # print(inner_pos)

                # print("QUADRANT 4 OUTER SPEED")
                # print(outer_speed)
                # print("QUADRANT 4 INNER SPEED")
                # print(inner_speed)

            
                # self.turn_r1.set(outer_pos)
                # self.turn_r2.set(-outer_pos)
                # self.turn_l1.set(inner_pos)
                # self.turn_l2.set(-inner_pos)

                self.power_r1.set(-outer_speed)
                self.power_r2.set(-outer_speed)
                self.power_l1.set(-inner_speed)
                self.power_l2.set(-inner_speed)
                #print("done3")

            else: # is in quadrant 3 

                

                for i in range(4):

                    real[i] = (turn_motors[i].getEncPosition() * ((2*math.pi)/self.TICKS_PER_REV)) % (2*math.pi) 

                    if real[i] > math.pi:

                        real[i] -= 2*math.pi

                adjustment_factors = [0,0,0,0]

                adjustment_factors[0] = inner_angle - real[0]
                adjustment_factors[1] = -inner_angle - real[1]
                adjustment_factors[2] = outer_angle - real[2]
                adjustment_factors[3] = -outer_angle - real[3]

                positions = [0,0,0,0]

                for i in range(4):

                    positions[i] = turn_motors[i].getEncPosition() + adjustment_factors[i] * self.TICKS_PER_REV/(2*math.pi)

                    turn_motors[i].set(positions[i])

                print("QUADRANT 3 OUTER POS")
                print(outer_pos)
                print("QUADRANT 3 INNER POS")
                print(inner_pos)

                print("QUADRANT 3 OUTER SPEED")
                print(outer_speed)
                print("QUADRANT 3 INNER SPEED")
                print(inner_speed)


                # self.turn_r1.set(inner_pos)
                # self.turn_r2.set(-inner_pos)
                # self.turn_l1.set(outer_pos)
                # self.turn_l2.set(-outer_pos)

                self.power_r1.set(-inner_speed)
                self.power_r2.set(-inner_speed)
                self.power_l1.set(-outer_speed)
                self.power_l2.set(-outer_speed)



    def strafe(self, joy_angle, power, scale_down):

        turn_motors = (self.turn_r1, self.turn_r2, self.turn_l1, self.turn_l2)
        power_motors = (self.power_r1, self.power_r2, self.power_l1, self.power_l2)

        for i in range(4):


            real = (turn_motors[i].getEncPosition() * ((2*math.pi)/self.TICKS_PER_REV)) % (2*math.pi) 

            power_motors[i].set(power*scale_down)

            if real > joy_angle:
                
                if (real-joy_angle) > math.pi:

                    adjustment_factor = ((2*math.pi - real) + joy_angle) * self.TICKS_PER_REV/(2*math.pi)

                    position = turn_motors[i].getEncPosition() + adjustment_factor
                    
                    turn_motors[i].set(position)
                else:
                    
                    adjustment_factor = (- (real - joy_angle)) * self.TICKS_PER_REV/(2*math.pi)

                    position = turn_motors[i].getEncPosition() + adjustment_factor
                    
                    turn_motors[i].set(position)
            else:
                
                if (joy_angle-real) > math.pi:
                    
                    adjustment_factor = (- real - (2*math.pi - joy_angle)) * self.TICKS_PER_REV/(2*math.pi)

                    position = turn_motors[i].getEncPosition() + adjustment_factor
                    
                    turn_motors[i].set(position)
                else:
                    
                    adjustment_factor = (joy_angle - real) * self.TICKS_PER_REV/(2*math.pi)

                    position = turn_motors[i].getEncPosition() + adjustment_factor
                    
                    turn_motors[i].set(position)


    def set_strafing(self, boolean):
        self.strafing = boolean

    def get_strafing(self):
        return self.strafing

    def switch_to_percentvbus(self):

        self.turn_r1.changeControlMode(CANTalon.ControlMode.PercentVbus)
        self.turn_r2.changeControlMode(CANTalon.ControlMode.PercentVbus)
        self.turn_l1.changeControlMode(CANTalon.ControlMode.PercentVbus)
        self.turn_l2.changeControlMode(CANTalon.ControlMode.PercentVbus)

        self.turn_r1.set(0)
        self.turn_r2.set(0)
        self.turn_l1.set(0)
        self.turn_l2.set(0)

    def set_enc_position(self, pos):

        self.turn_r1.setEncPosition(pos)
        self.turn_r2.setEncPosition(pos)
        self.turn_l1.setEncPosition(pos)
        self.turn_l2.setEncPosition(pos)

        #SWITCHES ALL TURN MOTORS BACK TO THE CORRECT CONTROL MODE

        self.turn_l2.changeControlMode(CANTalon.ControlMode.Position)
        self.turn_l2.setFeedbackDevice(CANTalon.FeedbackDevice.QuadEncoder)
        self.turn_l2.setPID(1.0, 0.0, 0.0)

        self.turn_r2.changeControlMode(CANTalon.ControlMode.Position)
        self.turn_r2.setFeedbackDevice(CANTalon.FeedbackDevice.QuadEncoder)
        self.turn_r2.setPID(1.0, 0.0, 0.0)

        self.turn_r1.changeControlMode(CANTalon.ControlMode.Position)
        self.turn_r1.setFeedbackDevice(CANTalon.FeedbackDevice.QuadEncoder)
        self.turn_r1.setPID(1.0, 0.0, 0.0)

        self.turn_l1.changeControlMode(CANTalon.ControlMode.Position)
        self.turn_l1.setFeedbackDevice(CANTalon.FeedbackDevice.QuadEncoder)
        self.turn_l1.setPID(1.0, 0.0, 0.0)
        
        #SETS THEM TO 0 JUST FOR FUN

        self.turn_r1.set(pos)
        self.turn_r2.set(pos)
        self.turn_l1.set(pos)
        self.turn_l2.set(pos)

    def zero(self):

        self.zeroing[0] = True
        self.zeroing[1] = True
        self.zeroing[2] = True
        self.zeroing[3] = True


        self.turn_r1.changeControlMode(CANTalon.ControlMode.PercentVbus)
        self.turn_r2.changeControlMode(CANTalon.ControlMode.PercentVbus)
        self.turn_l1.changeControlMode(CANTalon.ControlMode.PercentVbus)
        self.turn_l2.changeControlMode(CANTalon.ControlMode.PercentVbus)

        turning_power = .2

        self.turn_r1.set(turning_power)
        self.turn_r2.set(turning_power)
        self.turn_l1.set(turning_power)
        self.turn_l2.set(turning_power)

    def set_power(self, power):

        self.power_r1.set(power)
        self.power_r2.set(power)
        self.power_l1.set(power)
        self.power_l2.set(power)


    def _limit_listener(self, source, state_id, datum):

        if state_id == 'pressed' and datum and (self.zeroing[0] or self.zeroing[1] or self.zeroing[2] or self.zeroing[3]):

            #Positive: clockwise
            #Negative; counterclockwise

            if source == self.limit_r1 and self.zeroing[0]:

                print("r1 encoder position triggered")
                print(self.turn_r1.getEncPosition())
                #print(self.turn_r1.getEncPosition())

                self.turn_r1.setEncPosition(-1800) #-2050

                self.turn_r1.changeControlMode(CANTalon.ControlMode.Position)
                self.turn_r1.setFeedbackDevice(CANTalon.FeedbackDevice.QuadEncoder)
                self.turn_r1.setPID(1.0, 0.0, 0.0)

                self.turn_r1.set(0)

                self.zeroing[0] = False


                #cc: -1021, -1043, -1032, -1080, -935, -1006, -1034, -1057, -868, -990, -969, -910, -1006, -1070
                    # AVG: -1001.5 
                #c: -2122, -1970, -2087, -2012, -2130, -2085, -1999, -2022, -1987, -2050, -2085
                    # AVG: -2049.909090909091 

                #results: clockwise: 6616, 6621, 6583, 6569
                #         counterclockwise 7567, 7564, 7561, 7553

                # if self.turn_r1.getOutputVoltage() > 0:

                #     print("R1 ENCODER POSITION POSITIVE:")
                #     print(self.turn_r1.getEncPosition())
                #     #self.turn_r1.setEncPosition(6597 - 4096*50/24)

                # elif self.turn_r1.getOutputVoltage() < 0:

                #     print("R1 ENCODER POSITION NEGATIVE:")
                #     print(self.turn_r1.getEncPosition())
                #     #self.turn_r1.setEncPosition(7561 - 4096*50/24)


            if source == self.limit_r2 and self.zeroing[1]:

                print("r2 encoder position triggered")
                print(self.turn_r2.getEncPosition())

                self.turn_r2.setEncPosition(300) #-60

                self.turn_r2.changeControlMode(CANTalon.ControlMode.Position)
                self.turn_r2.setFeedbackDevice(CANTalon.FeedbackDevice.QuadEncoder)
                self.turn_r2.setPID(1.0, 0.0, 0.0)

                self.turn_r2.set(0)

                self.zeroing[1] = False

                #cc: 1246, 1265, 1256, 1298, 1266, 1324, 1333, 1313, 1346, 1307
                    #AVG: 1295.4
                    #WITH OLD: 1276.6
                #c: 21, 23, 2, -32, -31, -22, 35, -45, -54, -63, -136, -141, -163, -112, -128, -7, -168
                    #AVG: -60.05882352941177
                    #WITH OLD: -59.666666666666664

                #results: clockwise: -69, -63, -50, -50
                #        counterclockwise: 1239, 1261, 1238, 1208, 1249



                # if self.strafe_position > self.turn_r2.getEncPosition():       #self.turn_r2.getOutputVoltage() > 0:

                #     print("R2 ENCODER POSITION POSITIVE:")
                #     print(self.turn_r2.getEncPosition())
                #     #self.turn_r2.setEncPosition(58)

                # elif self.strafe_position < self.turn_r2.getEncPosition():        #self.turn_r2.getOutputVoltage() < 0:

                #     print("R2 ENCODER POSITION NEGATIVE:")
                #     print(self.turn_r2.getEncPosition())
                #     #self.turn_r2.setEncPosition(1239)

                # else:

                #     print("triggered w/o turning")

            if source == self.limit_l1 and self.zeroing[2]:

                print("l1 encoder position triggered")
                print(self.turn_l1.getEncPosition())

                self.turn_l1.setEncPosition(-4050) #-4197

                self.turn_l1.changeControlMode(CANTalon.ControlMode.Position)
                self.turn_l1.setFeedbackDevice(CANTalon.FeedbackDevice.QuadEncoder)
                self.turn_l1.setPID(1.0, 0.0, 0.0)

                self.turn_l1.set(0)

                self.zeroing[2] = False

                # cc: -3111, -3061, -3059, -3059, -3064, -3080, -3074, -3088, -3061 -3100
                    #AVG: -3075.7
                #  c: -4222, -4183, -4199, -4193, -4192, -4187, -4171, 4183, -4192, -4244
                    #AVG: -4196.6

                #results: clockwise: 4304, 4329, 4323, 4324
                #        counterclockwise: 5430, 5417, 5448, 5446

                # if self.turn_l1.getOutputVoltage() > 0:

                #     print("L1 ENCODER POSITION POSITIVE:")
                #     print(self.turn_l1.getEncPosition())
                #     #self.turn_l1.setEncPosition(4320 - 4096*50/24)

                # elif self.turn_l1.getOutputVoltage() < 0:

                #     print("L1 ENCODER POSITION NEGATIVE:")
                #     print(self.turn_l1.getEncPosition())
                #     #self.turn_l1.setEncPosition(5435 - 4096*50/24)

            if source == self.limit_l2 and self.zeroing[3]:

                print("l2 encoder position triggered")
                print(self.turn_l2.getEncPosition())

                self.turn_l2.setEncPosition(2500) #-2226

                self.turn_l2.changeControlMode(CANTalon.ControlMode.Position)
                self.turn_l2.setFeedbackDevice(CANTalon.FeedbackDevice.QuadEncoder)
                self.turn_l2.setPID(1.0, 0.0, 0.0)

                self.turn_l2.set(0)

                self.zeroing[3] = False

                #cc: 3370, 3390, 3400, 3362, 3356, 3371, 3370, 3353, 3379, 3379
                    #AVG: 3373.0
                    #AVG WITH OLD: 3367.8
                #c: 2240, 2255, 2239, 2208, 2228, 2243, 2232, 2236, 2227, 2250
                    #AVG: 2235.8
                    #AVG WITH OLD: 2226.4285714285716

                #results: clockwise: 2219, 2196, 2218, 2179
                #        counterclockwise: 3358, 3375, 3358, 3340, 3356

                # if self.turn_l2.getOutputVoltage() > 0:

                #     print("L2 ENCODER POSITION POSITIVE:")
                #     print(self.turn_l2.getEncPosition())
                #     #self.turn_l2.setEncPosition(2203)

                # elif self.turn_l2.getOutputVoltage() < 0:

                #     print("L2 ENCODER POSITION NEGATIVE:")
                #     print(self.turn_l2.getEncPosition())
                #     #self.turn_l2.setEncPosition(3357)

    #         #         #2048*50/24 = 4266