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

        self.HEIGHT = 1
        self.WIDTH = 2
        self.theta_1 = math.atan2(HEIGHT, WIDTH)
        self.theta_2 = math.pi - self.theta_1

    def _joylistener(self, sensor, state_id, datum):

        if state_id in ('x_axis', 'y_axis'):

            x = self.joystick.x_axis
            y = self.joystick.y_axis

            if abs(x) > .05 or abs(y) > .05:

                joy_angle = math.atan2(x, -y)

                power = math.sqrt(x**2 + y**2)

                ticks_per_rev = 4096*50/24 #I THINK SO!

                outer_angle = self.theta_1 * joy_angle/(math.pi/2)
                inner_angle = self.theta_2 * joy_angle/(math.pi/2)

                outer_speed = power
                inner_speed = power * math.sin(outer_angle)/math.sin(inner_angle)

                outer_pos = outer_angle*ticks_per_rev/(2*math.pi)
                inner_pos = inner_angle*ticks_per_rev/(2*math.pi)

                if abs(joy_angle) < math.pi/2:

                    if joy_angle >= 0:

                        self.turn_r1.set(outer_pos)
                        self.turn_r2.set(-outer_pos)
                        self.turn_l1.set(inner_pos)
                        self.turn_l2.set(-inner_pos)

                        self.power_r1.set(outer_speed)
                        self.power_r2.set(outer_speed)
                        self.power_l1.set(inner_speed)
                        self.power_l2.set(inner_speed)

                    else:

                        self.turn_l1.set(outer_pos)
                        self.turn_l2.set(-outer_pos)
                        self.turn_r1.set(inner_pos)
                        self.turn_r2.set(-inner_pos)

                        self.power_l1.set(outer_speed)
                        self.power_l2.set(outer_speed)
                        self.power_r1.set(inner_speed)
                        self.power_r2.set(inner_speed)

                #same as above but goes backwards
                else:

                    if joy_angle >= 0:

                        self.turn_r1.set(outer_pos)
                        self.turn_r2.set(-outer_pos)
                        self.turn_l1.set(inner_pos)
                        self.turn_l2.set(-inner_pos)

                        self.power_r1.set(-outer_speed)
                        self.power_r2.set(-outer_speed)
                        self.power_l1.set(-inner_speed)
                        self.power_l2.set(-inner_speed)

                    else:

                        self.turn_l1.set(outer_pos)
                        self.turn_l2.set(-outer_pos)
                        self.turn_r1.set(inner_pos)
                        self.turn_r2.set(-inner_pos)

                        self.power_l1.set(-outer_speed)
                        self.power_l2.set(-outer_speed)
                        self.power_r1.set(-inner_speed)
                        self.power_r2.set(-inner_speed)




    def _xbox_controller_listener(self, sensor, state_id, datum):

        if state_id == 'a_button':

            self.turn_r1.setEncPosition(0)
            self.turn_r2.setEncPosition(0)
            self.turn_l1.setEncPosition(0)
            self.turn_l2.setEncPosition(0)

