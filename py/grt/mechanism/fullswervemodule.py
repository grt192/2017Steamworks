from ctre import CANTalon
import math

class FullSwerveModule:

    def __init__(self, turn_r1, turn_r2, turn_l1, turn_l2, power_r1, power_r2, power_l1, power_l2, limit_r1=None, limit_r2=None, limit_l1=None, limit_l2=None):
        self.turn_r1 = turn_r1
        self.turn_r2 = turn_r2
        self.turn_l1 = turn_l1
        self.turn_l2 = turn_l2
        self.power_r1 = power_r1
        self.power_r2 = power_r2
        self.power_l1 = power_l1
        self.power_l2 = power_l2

        limit_r1.add_listener(self._limit_listener)
        limit_r2.add_listener(self._limit_listener)
        limit_l1.add_listener(self._limit_listener)
        limit_l2.add_listener(self._limit_listener)

        self.HEIGHT = 24
        self.WIDTH = 16
        self.DIAGONAL = math.sqrt(24**2 + 16**2)

        self.limit_r1_num = -6800
        self.limit_r2_num = 10800
        self.limit_l1_num = -15270
        self.limit_l2_num = 7850

    def full_swerve(self, joy_angle, joy_vector, rot_angle):
        turn_motors = (self.turn_r1, self.turn_r2, self.turn_l1, self.turn_l2)

        r1_x = power*math.cos(joy_angle) + DIAGONAL*rot_angle*cos(joy_angle+90)
        r1_x = power*math.sin(joy_angle) + DIAGONAL*rot_angle*sin(joy_angle+90)
        r1_tot = math.sqrt(r1_x**2 + r1_y**2)

        r1_ang = math.arctan(r1_x/r1_y)

