import math
from wpilib import CANTalon
import time

class SwerveDriveController:

    def __init__(self, l_joystick, r_joystick, dt=None):
        self.dt = dt
        self.l_joystick = l_joystick
        self. r_joystick = r_joystick

        self.l_joystick.add_listener(self._joylistener)
        self.r_joystick.add_listener(self._joylistener)

        self.vx
        self.vy
        self.angular_speed
        self.power = [0,0,0,0] #initialize the 4 motor powers to 0

        self.angle = [0,0,0,0] #initialize the 4 motor angles to 0

        '''

        The following constants are set to arbitrary values and must be measured
        
        '''

        self.r = [1,1,1,1]
        self.theta = [1,2,3,4]


        self.rotational_angle = [self.theta[0]+math.pi/2,self.theta[1]+math.pi/2,self.theta[2]+math.pi/2,self.theta[3]+math.pi/2]



    def _joylistener(self, sensor, state_id, datum):
        if sensor in (self.l_joystick, self.r_joystick) and state_id in ('x_axis', 'y_axis'):


            self.angular_speed = self.l_joystick.x_axis

                # x = [0,0,0,0]
                # y = [0,0,0,0]


            for i in range(4):
                x = self.r_joystick.x_axis + self.r[i]*self.angular_speed*math.cos(self.rotational_angle[i])
                y = self.r_joystick.y_axis + self.r[i]*self.angular_speed*math.sin(self.rotational_angle[i])
                self.power[i] = math.sqrt(x ** 2 + y ** 2)

                if x >= 0:
                    self.angle[i] = math.atan(y/x)

                else:
                    self.angle[i] = math.atan(y/x) + math.pi

                    

            for i in range(4):
                self.dt[i].set_power(self.power[i])
                self.dt[i].set_angle(self.angle[i])


class TestSwerveDriveController:

    def __init__(self, l_joystick, r_joystick, xbox_controller, dt=None, turn_motor=None, power_motor=None, turn_2 = None, turn_3 = None, limit_switch=None):
        self.dt = dt
        self.turn_motor = turn_motor
        self.turn_2 = turn_2
        self.turn_3 = turn_3
        self.power_motor = power_motor
        self.limit_switch = limit_switch
        self.l_joystick = l_joystick
        self. r_joystick = r_joystick
        self.xbox_controller = xbox_controller

        self.l_joystick.add_listener(self._joylistener)
        self.r_joystick.add_listener(self._joylistener)
        self.xbox_controller.add_listener(self._xbox_controller_listener)

       


    def _joylistener(self, sensor, state_id, datum):

        # THIS CODE IS CURRENTLY UNTESTED. WE WILL EVENTUALL SWITCH TO ATTACK JOYSTICKS, BUT FOR NOW THIS IS NOT USED.

        if sensor in (self.l_joystick, self.r_joystick) and state_id in ('x_axis', 'y_axis'):


                #self.angular_speed = self.l_joystick.x_axis



                x = self.l_joystick.x_axis
                y = self.l_joystick.y_axis

                # print(x)
                # print(y)

                if abs(x) > .05 and abs(y) > .05:

                    angle = math.atan2(x,-y)

                    power = math.sqrt(x ** 2 + y ** 2)

                    self.power_motor.set(power*.25)

                    ticks_per_rev = 4096*50/24 #I THINK SO!


                    position = angle*ticks_per_rev/(2*math.pi)
                    print(position)

                    

                    """
                    ZEROING INSTRUCTIONS:
                    1. Manually set zero. Robot should be off or disabled.
                    2. Comment out the 3 lines below that set positions of the turn motors and push code to robot.
                    3. Enable robot and press a to zero.
                    4. Uncomment these lines and repush the code to the robot.

                    Encoders should keep the zero that you just set and you will be able to control with attack jostyick.

                    """


                    self.turn_motor.set(position)
                    self.turn_2.set(position)
                    self.turn_3.set(position)

                else:
                    self.power_motor.set(0)

                # self.dt.set_power(power/(math.sqrt(2)))

                # self.dt.set_angle(angle)

    def _xbox_controller_listener(self, sensor, state_id, datum):
    
        #TURNING CONTROL WITH SWERVE USING THE ENCODER
        #THE 4096*50/24 IS WHAT I BELIEVE TO BE THE TICKS PER REVOLUTION, BUT I AM NOT 100% SURE
        #VALUES ARE SCALED DOWN BY .2 SO THAT THE ROBOT DOES NOT TURN TO FAST, BUT THIS LIMITS RANGE
        if state_id == 'l_x_axis':
            if abs(datum) > .1:
                position = datum*4096*50/24
                print("POSITION:")
                print(position)
                # self.turn_motor.set(position*.4) #.2
                # self.turn_2.set(position*.4)
                # self.turn_3.set(position*.4)

        #POWER CONTROL OF THE SWERVE MODULE
        elif state_id == 'r_y_axis':
            if abs(datum) > .05:
                print("going forward")
                self.power_motor.set(datum*.5) #.3

            else:
                self.power_motor.set(0)

        #ZEROING OF THE ENCODER
        elif state_id == 'a_button':
            if datum:
                self.turn_motor.setEncPosition(0)
                self.turn_2.setEncPosition(0)
                self.turn_3.setEncPosition(0)
                print("Zeroing:")
                print(self.turn_motor.getEncPosition())
                # self.turn_motor.set(0)
                # self.turn_2.set(0)
                # self.turn_3.set(0)

        #INCREMENT THE TURN MOTOR BY A SET AMOUNT
        elif state_id == 'b_button':
            if datum:
                
                self.turn_motor.set(self.turn_motor.getEncPosition() + 1024*4)
                
        #DECREMENT THE TURN MOTOR BY A SET AMOUNT
        elif state_id == 'x_button':
            if datum: 
                
                self.turn_motor.set(self.turn_motor.getEncPosition() - 1024*4)
                

        elif state_id == 'y_button':
            if datum:
                print("ENCODER POSITION:")
                print(self.turn_motor.getEncPosition())

        elif state_id == "w_button":
            if datum:
                self.turn_motor.set_zero()


