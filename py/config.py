"""
Config File for Robot
"""

from wpilib import Solenoid, Compressor, DriverStation, DigitalInput
from ctre import CANTalon

from grt.sensors.attack_joystick import Attack3Joystick
from grt.sensors.xbox_joystick import XboxJoystick
#from grt.sensors.gyro import Gyro
from grt.core import SensorPoller
from grt.mechanism.swervemodule import SwerveModule 
from grt.mechanism.drivetrain import DriveTrain
from grt.mechanism.drivecontroller import ArcadeDriveController
from grt.mechanism.motorset import Motorset
from grt.sensors.ticker import Ticker
from grt.sensors.encoder import Encoder
#from grt.sensors.talon import Talon
from grt.mechanism.mechcontroller import MechController
from grt.mechanism.swervecontroller import TestSwerveDriveController
from grt.mechanism.ackermancontroller import AckermanController
from grt.mechanism.beta_mechs import Shooter, Intake, Gear, Climber, Hopper
from grt.mechanism import ZeroTest, TalonTester
from grt.sensors.switch import Switch
from grt.mechanism.new_ackermancontroller import NewAckermanController

from grt.autonomous.basic_auto import BasicAuto



#DT Talons and Objects

#OMEGA 2

# TALON ASSIGNMENT:


# 1: front right dt power
# 2: back left dt power
# 3: back right dt turn
# 4: CLIMBER WOOOOHHOOOOOOOO!!!!!!!!!!!
# 5: front left dt power
# 6: front shooter (wrong direction)
# 7: intake
# 8: integration roller
# 9: front right dt turn
# 10: front left dt turn
# 11: CLIMBER WOOOHHOOOOOOOO!!!!!!!!!!!!! part 2 lmao
# 12: back left dt turn
# 13: back shooter
# 14: back right dt power


#SOLENOID ASSIGNMENT:

# o:
# 1:
# 2: 
# 3: gear 
# 4: gear indexer

#OMEGA 1

# 1: front right power
# 2: climber1
# 3: front right turn
# 4: intake
# 5: climber2
# 6: back left power
# 7: front left turn
# 8: inegration
# 9: shooter 2
# 10: back left turn
# 11: shooter 1
# 12: disk
# 13: front left power
# 14: back right power
# 15: back right turn


#SOLENOID ASSIGNMENT:

# o:
# 1:
# 2: 
# 3: gear 
# 4: gear indexer


#test_solenoid = Solenoid(4)

#test_motor = CANTalon(15)

talon_test = TalonTester(motor=None)

#talon order: tl2,tr2,tl,tr,dr,dl,dr2,dl2,s1,s2,l,d,i,c,c2

omega_2_talons = [12,3,10,9,1,5,2,14,6,13,8,15,7,4,11]

talons = omega_2_talons


#UNCOMMENT THE FOLLOWING LATER
turn_l2 = CANTalon(10) 
turn_l2.changeControlMode(CANTalon.ControlMode.Position)
turn_l2.setFeedbackDevice(CANTalon.FeedbackDevice.QuadEncoder)
turn_l2.setPID(1.0, 0.0, 0.0)

turn_r2 = CANTalon(15)
turn_r2.changeControlMode(CANTalon.ControlMode.Position)
turn_r2.setFeedbackDevice(CANTalon.FeedbackDevice.QuadEncoder)
turn_r2.setPID(1.0, 0.0, 0.0)

turn_left = CANTalon(7)
turn_left.changeControlMode(CANTalon.ControlMode.Position)
turn_left.setFeedbackDevice(CANTalon.FeedbackDevice.QuadEncoder)
turn_left.setPID(1.0, 0.0, 0.0)

turn_right = CANTalon(3)#5
turn_right.changeControlMode(CANTalon.ControlMode.Position)
turn_right.setFeedbackDevice(CANTalon.FeedbackDevice.QuadEncoder)
turn_right.setPID(1.0, 0.0, 0.0)


#TAKEN FOR TURNING: 8 9 2 5
#AVAILABLE: 

#front right 6 turning: 5
#front left 1 turning: 2
#back right 7 turning: 9
#back left 4 turning: 8

dt_right = CANTalon(1)
dt_left = CANTalon(13)

dt_l2 = CANTalon(6)
dt_r2 = CANTalon(14)


shooter1_m1 = CANTalon(11)
shooter1_m2 = CANTalon(9)
# shooter2_m1 = CANTalon(20)
# shooter2_m2 = CANTalon(20)

shooter1_m1.changeControlMode(CANTalon.ControlMode.Speed)
shooter1_m1.setPID(1.0,0.008,20, f=0.47383)
#shooter1_m1.setPID(0.20, 0.001, 0)
# shooter1_m1.setPID(.33, 0, 0, f=.17)

shooter1_m2.changeControlMode(CANTalon.ControlMode.Speed)
#shooter1_m2.setPID(0,0,0)
shooter1_m2.setPID(1.0,0.008,20, f=0.478037)
#shooter1_m2.setPID(0.20, 0.001, 0)
# shooter1_m2.setPID(.33, 0, 0, f=.17)

# shooter2_m1.changeControlMode(CANTalon.ControlMode.Speed)
# shooter2_m1.setPID(.33, 0, 0, f=.17)

# shooter2_m2.changeControlMode(CANTalon.ControlMode.Speed)
# shooter2_m2.setPID(.33, 0, 0, f=.17)

load_m = CANTalon(8)
# load_m.reverseOutput(True)

disk_m = CANTalon(12)
# disk_m.changeControlMode(CANTalon.ControlMode.Follower)
# disk_m.set(load_m.getDeviceID())

angle_change = Solenoid(0)

shooter = Shooter(shooter1_m1, shooter1_m2, load_m, angle_change, disk_m)

intake_motor = CANTalon(4)

intake = Intake(intake_motor)




climber_motor = CANTalon(2)

c2 = CANTalon(5)

c2.changeControlMode(CANTalon.ControlMode.Follower)
c2.set(climber_motor.getDeviceID())

climber = Climber(climber_motor)


gear_pneumatic_1 = Solenoid(2)
gear_pneumatic_2 = Solenoid(1)

gear_mech = Gear(gear_pneumatic_1, gear_pneumatic_2)


hopper_pneumatic = Solenoid(3)


hopper = Hopper(hopper_pneumatic)

#omega 2: 9,2,0,1

limit_r1 = Switch(1) #I messed up the wiring
limit_r2 = Switch(2, reverse=True)
limit_l1 = Switch(3, reverse=True)
limit_l2 = Switch(4)

#zero_test = ZeroTest(turn_right, limit_switch)



#needs to be changed for left and right
tank_dt = DriveTrain(dt_left, dt_right, left_shifter=None, left_encoder=None, right_encoder=None)
#Skeleton sensor poller
#gyro = Gyro(1)
# define sensor poller
# sp = SensorPoller()

swerve = SwerveModule(turn_right, turn_r2, turn_left, turn_l2, dt_right, dt_r2, dt_left, dt_l2, limit_r1 = limit_r1, limit_r2 = limit_r2, limit_l1 = limit_l1, limit_l2 = limit_l2)



# Drive Controllers
l_joystick = Attack3Joystick(0)

#r_joystick = Attack3Joystick(3)
xbox_controller = XboxJoystick(1)
xbox_controller_2 = XboxJoystick(2)
#ac = ArcadeDriveController(tank_dt, l_joystick)
hid_sp = SensorPoller((l_joystick, xbox_controller, xbox_controller_2))  # human interface devices
sp = SensorPoller((limit_r1, limit_r2, limit_l1, limit_l2))


basic_auto = BasicAuto(swerve)

# Mech Talons, objects, and controller

#sc = TestSwerveDriveController(l_joystick, r_joystick, xbox_controller, dt=dt, turn_motor=turn_motor, power_motor=power_motor, turn_2 = turn_2, turn_3 = turn_3)

#ac = AckermanController(l_joystick, xbox_controller, turn_right, turn_r2, turn_left, turn_l2, dt_right, dt_r2, dt_left, dt_l2, limit_r1, limit_r2, limit_l1, limit_l2)

new_ac = NewAckermanController(l_joystick, xbox_controller, swerve)

# define MechController
mc = MechController(l_joystick, xbox_controller_2, shooter, intake, gear_mech, hopper, climber=climber, talon_test=talon_test)

# define DriverStation
ds = DriverStation.getInstance()





