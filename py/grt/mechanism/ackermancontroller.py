import math
from wpilib import CANTalon

class AckermanController:

    def __init__(self, joystick, xbox_controller, turn_r1, turn_r2, turn_l1, turn_l2, power_r1, power_r2, power_l1, power_l2, limit_r1, limit_r2, limit_l1, limit_l2):

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

        # limit_r1.add_listener(self._limit_listener)
        # limit_r2.add_listener(self._limit_listener)
        # limit_l1.add_listener(self._limit_listener)
        # limit_l2.add_listener(self._limit_listener)

        self.joystick = joystick
        self.xbox_controller = xbox_controller

        self.joystick.add_listener(self._joylistener)
        self.xbox_controller.add_listener(self._xbox_controller_listener)

        self.HEIGHT = 21
        self.WIDTH = 25

        #MAX ANGLE FOR OUTSIDE WHEEL
        self.theta_1 = math.atan2(self.HEIGHT, self.WIDTH)

        #MAX ANGLE FOR INSIDE WHEEL
        self.theta_2 = math.pi - self.theta_1

        self.strafing = False

        self.strafe_position = 0

        self.TICKS_PER_REV = 4096*50/24 #I THINK SO!

    def _joylistener(self, sensor, state_id, datum):

        pass


    def _xbox_controller_listener(self, sensor, state_id, datum):

        #TO ZERO: press B, move to correct positions, then press A

        if state_id == 'a_button':

            if datum:

                #SETS ENCODER POSITIONS TO 0

                self.turn_r1.setEncPosition(0)
                self.turn_r2.setEncPosition(0)
                self.turn_l1.setEncPosition(0)
                self.turn_l2.setEncPosition(0)

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

                # self.turn_r1.set(0)
                # self.turn_r2.set(0)
                # self.turn_l1.set(0)
                # self.turn_l2.set(0)

        elif state_id == 'b_button':

            if datum: 

                #SWITCHS CONTROL MODE AND SETS POWER TO 0 SO THAT THEY CAN BE MOVED

                self.turn_r1.changeControlMode(CANTalon.ControlMode.PercentVbus)
                self.turn_r2.changeControlMode(CANTalon.ControlMode.PercentVbus)
                self.turn_l1.changeControlMode(CANTalon.ControlMode.PercentVbus)
                self.turn_l2.changeControlMode(CANTalon.ControlMode.PercentVbus)

                self.turn_r1.set(0)
                self.turn_r2.set(0)
                self.turn_l1.set(0)
                self.turn_l2.set(0)

        #MANUAL SWITCH TO STRAFING

        elif state_id == 'x_button':

            if datum:

                    self.strafing = True
                    print("SWITCHED TO STRAFING")

        #MANUAL SWITCH TO ACKERMAN

        elif state_id == 'y_button':

            if datum:

                self.strafing = False
                print("SWITCHED TO ACKERMAN")

        #RIGHT JOYSTICK FOR STRAFING

        elif state_id in ('r_y_axis', 'r_x_axis'):

            
            x = self.xbox_controller.r_x_axis
            y = self.xbox_controller.r_y_axis

            """

            
            if abs(x) > .2 or abs(y) > .2:

                self.strafing = True
                # print("SWITCHED TO STRAFING")

                

                angle = math.atan2(x,-y)
                

                power = math.sqrt(x ** 2 + y ** 2)

                self.strafe_position = angle * self.TICKS_PER_REV / (2*math.pi)
               

                #USES MOTOR TURN_R1 TO DETERMIN THE CURRENT POSITION.
                #Not sure if it would be better to do this individually for each motor.

                cur_angle = self.turn_l2.getEncPosition()*(2*math.pi)/self.TICKS_PER_REV

                #IF THE WHEEL IS CURRENTLY IN Q3 OR Q4 AND NEEDS TO GO TO THE OTHER ONE

                if (abs(cur_angle) > math.pi/2) and (abs(self.strafe_position) > (self.TICKS_PER_REV/4)) and (cur_angle * self.strafe_position < 0): 

                    #print("resetting enc pos")
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


                
                self.turn_r1.set(self.strafe_position)
                self.turn_r2.set(self.strafe_position)
                self.turn_l1.set(self.strafe_position)
                self.turn_l2.set(self.strafe_position)

                self.power_r1.set(power*.5)
                self.power_r2.set(power*.5)
                self.power_l1.set(power*.5)
                self.power_l2.set(power*.5)


            else:

                self.turn_r1.set(0)
                self.turn_r2.set(0)
                self.turn_l1.set(0)
                self.turn_l2.set(0)

                self.power_r1.set(0)
                self.power_r2.set(0)
                self.power_l1.set(0)
                self.power_l2.set(0)

                self.strafing = False
                #print("SWITCHED TO ACKERMAN")


            """   
            
            angle = math.atan2(x,-y) % (2*math.pi)
            print("angle")
            print(angle)

            turn_motors = (self.turn_r1, self.turn_r2, self.turn_l1, self.turn_l2)
            power_motors = (self.power_r1, self.power_r2, self.power_l1, self.power_l2)

            for i in range(4):


                real = (turn_motors[i].getEncPosition() * ((2*math.pi)/self.TICKS_PER_REV)) % (2*math.pi) 

                if abs(x) > .2 or abs(y) > .2:

                    power = math.sqrt(x ** 2 + y ** 2)

                    power_motors[i].set(power*.4)

                    if real > angle:
                        
                        if (real-angle) > math.pi:

                            adjustment_factor = ((2*math.pi - real) + angle) * self.TICKS_PER_REV/(2*math.pi)

                            position = turn_motors[i].getEncPosition() + adjustment_factor
                            
                            turn_motors[i].set(position)
                        else:
                            
                            adjustment_factor = (- (real - angle)) * self.TICKS_PER_REV/(2*math.pi)

                            position = turn_motors[i].getEncPosition() + adjustment_factor
                            
                            turn_motors[i].set(position)
                    else:
                        
                        if (angle-real) > math.pi:
                            
                            adjustment_factor = (- real - (2*math.pi - angle)) * self.TICKS_PER_REV/(2*math.pi)

                            position = turn_motors[i].getEncPosition() + adjustment_factor
                            
                            turn_motors[i].set(position)
                        else:
                            
                            adjustment_factor = (angle - real) * self.TICKS_PER_REV/(2*math.pi)

                            position = turn_motors[i].getEncPosition() + adjustment_factor
                            
                            turn_motors[i].set(position)

                else:

                    power_motors[i].set(0)

                    if real > math.pi:

                        adjustment_factor = (2*math.pi - real) * self.TICKS_PER_REV/(2*math.pi)

                        position = turn_motors[i].getEncPosition() + adjustment_factor

                        turn_motors[i].set(position)

                    else:

                        adjustment_factor = (-real) * self.TICKS_PER_REV/(2*math.pi)

                        position = turn_motors[i].getEncPosition() + adjustment_factor

                        turn_motors[i].set(position)




        elif state_id in ('l_y_axis', 'l_x_axis'):

            x = self.xbox_controller.l_x_axis
            y = self.xbox_controller.l_y_axis

            real = [0,0,0,0]

            turn_motors = (self.turn_r1, self.turn_r2, self.turn_l1, self.turn_l2)

            if (abs(x) > .2 or abs(y) > .2) and  not self.strafing:

                joy_angle = math.atan2(x, -y)
                # print("JOY ANGLE")
                # print(joy_angle)

                #DETERMINE POWER: size of vector based on joystick x and y

                power = math.sqrt(x**2 + y**2)

                

                #CASES FOR QUADRANTS 1 AND 4

                #NOTE ABOUT PHILOSOPHY: 
                #rather than have the wheel spin 360, it stays within an 180 degree range, 
                #but goes backwards for going backwards.

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
                        #print("done4")

            else:

                for i in range(4):

                    print("Getting here")

                    adjustment_factor = -real[i] * self.TICKS_PER_REV/(2*math.pi)

                    position = turn_motors[i].getEncPosition() + adjustment_factor

                    turn_motors[i].set(position)



                # self.turn_r1.set(0)
                # self.turn_r2.set(0)
                # self.turn_l1.set(0)
                # self.turn_l2.set(0)

                self.power_r1.set(0)
                self.power_r2.set(0)
                self.power_l1.set(0)
                self.power_l2.set(0)

    # def _limit_listener(self, source, state_id, datum):

    #     if state_id == 'pressed' and datum:

    #         #Positive: clockwise
    #         #Negative; counterclockwise

    #         if source == self.limit_r1:

    #             print("r1 encoder position triggered")
    #             print(self.turn_r1.getEncPosition())

    #             #cc: -1021, -1043, -1032, -1080, -935, -1006, -1034, -1057, -868, -990, -969, -910, -1006, -1070
    #                 # AVG: -1001.5 
    #             #c: -2122, -1970, -2087, -2012, -2130, -2085, -1999, -2022, -1987, -2050, -2085
    #                 # AVG: -2049.909090909091 

    #             #results: clockwise: 6616, 6621, 6583, 6569
    #             #         counterclockwise 7567, 7564, 7561, 7553

    #             if self.turn_r1.getOutputVoltage() > 0:

    #                 print("R1 ENCODER POSITION POSITIVE:")
    #                 print(self.turn_r1.getEncPosition())
    #                 #self.turn_r1.setEncPosition(6597 - 4096*50/24)

    #             elif self.turn_r1.getOutputVoltage() < 0:

    #                 print("R1 ENCODER POSITION NEGATIVE:")
    #                 print(self.turn_r1.getEncPosition())
    #                 #self.turn_r1.setEncPosition(7561 - 4096*50/24)


    #         if source == self.limit_r2:

    #             print("r2 encoder position triggered")
    #             print(self.turn_r2.getEncPosition())

    #             #cc: 1246, 1265, 1256, 1298, 1266, 1324, 1333, 1313, 1346, 1307
    #                 #AVG: 1295.4
    #                 #WITH OLD: 1276.6
    #             #c: 21, 23, 2, -32, -31, -22, 35, -45, -54, -63, -136, -141, -163, -112, -128, -7, -168
    #                 #AVG: -60.05882352941177
    #                 #WITH OLD: -59.666666666666664

    #             #results: clockwise: -69, -63, -50, -50
    #             #        counterclockwise: 1239, 1261, 1238, 1208, 1249

    #             if self.strafe_position > self.turn_r2.getEncPosition():       #self.turn_r2.getOutputVoltage() > 0:

    #                 print("R2 ENCODER POSITION POSITIVE:")
    #                 print(self.turn_r2.getEncPosition())
    #                 #self.turn_r2.setEncPosition(58)

    #             elif self.strafe_position < self.turn_r2.getEncPosition():        #self.turn_r2.getOutputVoltage() < 0:

    #                 print("R2 ENCODER POSITION NEGATIVE:")
    #                 print(self.turn_r2.getEncPosition())
    #                 #self.turn_r2.setEncPosition(1239)

    #             else:

    #                 print("triggered w/o turning")

    #         if source == self.limit_l1:

    #             print("l1 encoder position triggered")
    #             print(self.turn_l1.getEncPosition())

    #             # cc: -3111, -3061, -3059, -3059, -3064, -3080, -3074, -3088, -3061 -3100
    #                 #AVG: -3075.7
    #             #  c: -4222, -4183, -4199, -4193, -4192, -4187, -4171, 4183, -4192, -4244
    #                 #AVG: -4196.6

    #             #results: clockwise: 4304, 4329, 4323, 4324
    #             #        counterclockwise: 5430, 5417, 5448, 5446

    #             if self.turn_l1.getOutputVoltage() > 0:

    #                 print("L1 ENCODER POSITION POSITIVE:")
    #                 print(self.turn_l1.getEncPosition())
    #                 #self.turn_l1.setEncPosition(4320 - 4096*50/24)

    #             elif self.turn_l1.getOutputVoltage() < 0:

    #                 print("L1 ENCODER POSITION NEGATIVE:")
    #                 print(self.turn_l1.getEncPosition())
    #                 #self.turn_l1.setEncPosition(5435 - 4096*50/24)

    #         if source == self.limit_l2:

    #             print("l2 encoder position triggered")
    #             print(self.turn_l2.getEncPosition())

    #             #cc: 3370, 3390, 3400, 3362, 3356, 3371, 3370, 3353, 3379, 3379
    #                 #AVG: 3373.0
    #                 #AVG WITH OLD: 3367.8
    #             #c: 2240, 2255, 2239, 2208, 2228, 2243, 2232, 2236, 2227, 2250
    #                 #AVG: 2235.8
    #                 #AVG WITH OLD: 2226.4285714285716

    #             #results: clockwise: 2219, 2196, 2218, 2179
    #             #        counterclockwise: 3358, 3375, 3358, 3340, 3356

    #             if self.turn_l2.getOutputVoltage() > 0:

    #                 print("L2 ENCODER POSITION POSITIVE:")
    #                 print(self.turn_l2.getEncPosition())
    #                 #self.turn_l2.setEncPosition(2203)

    #             elif self.turn_l2.getOutputVoltage() < 0:

    #                 print("L2 ENCODER POSITION NEGATIVE:")
    #                 print(self.turn_l2.getEncPosition())
    #                 #self.turn_l2.setEncPosition(3357)

    #         #         #2048*50/24 = 4266