"""
Config File for Robot
"""

from wpilib import Solenoid, Compressor, DriverStation, CANTalon

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


#DT Talons and Objects


#UNCOMMENT THE FOLLOWING LATER
turn_l2 = CANTalon(8) #8
turn_l2.changeControlMode(CANTalon.ControlMode.Position)
turn_l2.setFeedbackDevice(CANTalon.FeedbackDevice.QuadEncoder)
turn_l2.setPID(1.0, 0.0, 0.0)

turn_r2 = CANTalon(9) #9
turn_r2.changeControlMode(CANTalon.ControlMode.Position)
turn_r2.setFeedbackDevice(CANTalon.FeedbackDevice.QuadEncoder)
turn_r2.setPID(1.0, 0.0, 0.0)

turn_left = CANTalon(2) #2
turn_left.changeControlMode(CANTalon.ControlMode.Position)
turn_left.setFeedbackDevice(CANTalon.FeedbackDevice.QuadEncoder)
turn_left.setPID(1.0, 0.0, 0.0)

turn_right = CANTalon(5) #5
turn_right.changeControlMode(CANTalon.ControlMode.Position)
turn_right.setFeedbackDevice(CANTalon.FeedbackDevice.QuadEncoder)
turn_right.setPID(1.0, 0.0, 0.0)


#TAKEN FOR TURNING: 8 9 2 5
#AVAILABLE: 

#front right 6 turning: 5
#front left 1 turning: 2
#back right 7 turning: 9
#back left 4 turning: 8

dt_right = CANTalon(6) 
dt_left = CANTalon(1) 

dt_l2 = CANTalon(4) 
dt_r2 = CANTalon(7) 


shooter1_m1 = CANTalon(10)
shooter1_m2 = CANTalon(11)
shooter2_m1 = CANTalon(12)
shooter2_m2 = CANTalon(13)

shooter1_m1.changeControlMode(CANTalon.ControlMode.Speed)
shooter1_m1.setPID(.33, 0, 0, f=.17)

shooter1_m2.changeControlMode(CANTalon.ControlMode.Speed)
shooter1_m2.setPID(.33, 0, 0, f=.17)

shooter2_m1.changeControlMode(CANTalon.ControlMode.Speed)
shooter2_m1.setPID(.33, 0, 0, f=.17)

shooter2_m2.changeControlMode(CANTalon.ControlMode.Speed)
shooter2_m2.setPID(.33, 0, 0, f=.17)

load_m = CANTalon(14)

shooter = Shooter(shooter1_m1, shooter1_m2, shooter2_m1, shooter2_m2, load_m)


intake_motor = CANTalon(15)

intake = Intake(intake_motor)


climber_motor = CANTalon(16)

c2 = CANTalon(17)

c2.changeControlMode(CANTalon.changeControlMode.Follower)
c2.set(climber_motor.getDeviceID())

climber = Climber(climber_motor)


gear_pneumatic_1 = Solenoid(0)
gear_pneumatic_2 = Solenoid(1)

gear_mech = Gear(gear_pneumatic_1, gear_pneumatic_2)


hopper_pneumatic = Solenoid(2)

hopper = Hopper(hopper_pneumatic)



#dt = SwerveModule(power_motor, turn_motor)

#needs to be changed for left and right
tank_dt = DriveTrain(dt_left, dt_right, left_shifter=None, left_encoder=None, right_encoder=None)
#Skeleton sensor poller
#gyro = Gyro(1)
# define sensor poller
# sp = SensorPoller()


# Drive Controllers
l_joystick = Attack3Joystick(0)
r_joystick = Attack3Joystick(3)
xbox_controller = XboxJoystick(1)
#ac = ArcadeDriveController(tank_dt, l_joystick)
hid_sp = SensorPoller((l_joystick, r_joystick, xbox_controller))  # human interface devices



# Mech Talons, objects, and controller

#sc = TestSwerveDriveController(l_joystick, r_joystick, xbox_controller, dt=dt, turn_motor=turn_motor, power_motor=power_motor, turn_2 = turn_2, turn_3 = turn_3)

ac = AckermanController(l_joystick, xbox_controller, turn_right, turn_r2, turn_left, turn_l2, dt_right, dt_r2, dt_left, dt_l2)

# define MechController
#mc = MechController(l_joystick, xbox_controller, turn_motor, turn_2, turn_3, turn_4)

# define DriverStation
ds = DriverStation.getInstance()





