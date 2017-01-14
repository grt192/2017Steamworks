import math
from wpilib import CANTalon

class AckermanController:

    def __init__(self, joystick, xbox_controller, turn_r1, turn_r2, turn_l1, turn_l2, power_r1, power_r2, power_l1, power_l2):

        self.turn_r1 = turn_r1
        self.turn_r2 = turn_r2
        self.turn_l1 = turn_l1
        self.turn_l2 = turn_l2

        self.power_r1 = power_r1
        self.power_r2 = power_r2
        self.power_l1 = power_l1
        self.power_l2 = power_l2

        self.joystick = joystick
        self.xbox_controller = xbox_controller

        self.joystick.add_listener(self._joylistener)
        self.xbox_controller.add_listener(self._xbox_controller_listener)

        self.HEIGHT = 24
        self.WIDTH = 16
        self.theta_1 = math.atan2(self.HEIGHT, self.WIDTH)
        self.theta_2 = math.pi - self.theta_1

    def _joylistener(self, sensor, state_id, datum):

        if state_id in ('x_axis', 'y_axis'):

            x = self.joystick.x_axis
            y = self.joystick.y_axis

            if abs(x) > .05 or abs(y) > .05:

                joy_angle = math.atan2(x, -y)
                print("JOY ANGLE")
                print(joy_angle)

                power = math.sqrt(x**2 + y**2)

                # print("POWER")
                # print(power)

                TICKS_PER_REV = 4096*50/24 #I THINK SO!

                outer_angle = self.theta_1 * joy_angle/(math.pi/2)
                inner_angle = self.theta_2 * joy_angle/(math.pi/2)

                # print("OUTER ANGLE")
                # print(outer_angle)

                # print("INNER ANGLE")
                # print(inner_angle)

                outer_speed = power

                if inner_angle == 0:
                    inner_speed = power
                else:
                    inner_speed = power * math.sin(outer_angle)/math.sin(inner_angle)

                # print("OUTER SPEED")
                # print(outer_speed)

                # print("INNER SPEED")
                # print(inner_speed)

                outer_pos = outer_angle*TICKS_PER_REV/(2*math.pi)
                inner_pos = inner_angle*TICKS_PER_REV/(2*math.pi)

                # print("OUTER POSITION")
                # print(outer_pos)

                # print("INNER POSITION")
                # print(inner_pos)

                if abs(joy_angle) < math.pi/2: #is in quadrant 1 or 2

                    if joy_angle <= 0: #is in quadrant 2

                        self.turn_r1.set(outer_pos)
                        self.turn_r2.set(-outer_pos)
                        self.turn_l1.set(inner_pos)
                        self.turn_l2.set(-inner_pos)

                        self.power_r1.set(outer_speed)
                        self.power_r2.set(outer_speed)
                        self.power_l1.set(inner_speed)
                        self.power_l2.set(inner_speed)
                        #print("done1")

                    else: # is in quadrant 1

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

                    inner_pos = TICKS_PER_REV/2 - inner_pos
                    outer_pos = TICKS_PER_REV/2 - outer_pos

                    if joy_angle >= 0: # is in quadrant 4

                        

                        self.turn_r1.set(inner_pos)
                        self.turn_r2.set(-inner_pos)
                        self.turn_l1.set(outer_pos)
                        self.turn_l2.set(-outer_pos)

                        self.power_r1.set(-inner_speed)
                        self.power_r2.set(-inner_speed)
                        self.power_l1.set(-outer_speed)
                        self.power_l2.set(-outer_speed)
                        #print("done3")

                    else: # is in quadrant 3 



                        self.turn_r1.set(outer_pos)
                        self.turn_r2.set(-outer_pos)
                        self.turn_l1.set(inner_pos)
                        self.turn_l2.set(-inner_pos)

                        self.power_r1.set(-outer_speed)
                        self.power_r2.set(-outer_speed)
                        self.power_l1.set(-inner_speed)
                        self.power_l2.set(-inner_speed)
                        #print("done4")

            else:

                self.power_l1.set(0)
                self.power_l2.set(0)
                self.power_r1.set(0)
                self.power_r2.set(0)





    def _xbox_controller_listener(self, sensor, state_id, datum):

        if state_id == 'a_button':

            self.turn_r1.setEncPosition(0)
            self.turn_r2.setEncPosition(0)
            self.turn_l1.setEncPosition(0)
            self.turn_l2.setEncPosition(0)

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
 

            self.turn_r1.set(0)
            self.turn_r2.set(0)
            self.turn_l1.set(0)
            self.turn_l2.set(0)

        elif state_id == 'b_button':

            self.turn_r1.changeControlMode(CANTalon.ControlMode.PercentVbus)
            self.turn_r2.changeControlMode(CANTalon.ControlMode.PercentVbus)
            self.turn_l1.changeControlMode(CANTalon.ControlMode.PercentVbus)
            self.turn_l2.changeControlMode(CANTalon.ControlMode.PercentVbus)

