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


#DT Talons and Objects

turn_motor = CANTalon(6)
turn_motor.changeControlMode(CANTalon.ControlMode.Position)
turn_motor.setFeedbackDevice(CANTalon.FeedbackDevice.QuadEncoder)
turn_motor.setPID(1.0, 0.0, 0.0)
#turn_motor.setPID(80, 0, 0, f=0)

# turn_motor.configMaxOutputVoltage(8)
# turn_motor.setAllowableClosedLoopErr(1)
# turn_motor.reverseOutput(True)

limit_switch = DigitalInput(5)


power_motor = CANTalon(6)

turn_2 = CANTalon(2)
turn_2.changeControlMode(CANTalon.ControlMode.Position)
turn_2.setFeedbackDevice(CANTalon.FeedbackDevice.QuadEncoder)
turn_2.setPID(1.0, 0.0, 0.0)
turn_3 = CANTalon(9)
turn_3.changeControlMode(CANTalon.ControlMode.Position)
turn_3.setFeedbackDevice(CANTalon.FeedbackDevice.QuadEncoder)
turn_3.setPID(1.0, 0.0, 0.0)
#turn_4 = CANTalon(5)

power_2 = CANTalon(1)
power_3 = CANTalon(7)
power_4 = CANTalon(8)


# turn_2.changeControlMode(CANTalon.ControlMode.Follower)
# turn_3.changeControlMode(CANTalon.ControlMode.Follower)
# #turn_4.changeControlMode(CANTalon.ControlMode.Fol                          lower)

power_3.changeControlMode(CANTalon.ControlMode.Follower)
power_4.changeControlMode(CANTalon.ControlMode.Follower)
#power_4.changeControlMode(CANTalon.ControlMode.Follower)

# turn_2.set(8)
# turn_3.set(8)
# #turn_4.set(8)

power_3.set(6)
power_4.set(7)
#.set(6)

dt = SwerveModule(power_motor, turn_motor)

#needs to be changed for left and right
tank_dt = DriveTrain(power_motor, power_2, left_shifter=None, left_encoder=None, right_encoder=None)
#Skeleton sensor poller
#gyro = Gyro(1)
# define sensor poller
# sp = SensorPoller()


# Drive Controllers
l_joystick = Attack3Joystick(0)
r_joystick = Attack3Joystick(3)
xbox_controller = XboxJoystick(1)
ac = ArcadeDriveController(tank_dt, l_joystick)
hid_sp = SensorPoller((l_joystick, r_joystick, xbox_controller))  # human interface devices



# Mech Talons, objects, and controller

#sc = TestSwerveDriveController(l_joystick, r_joystick, xbox_controller, dt=dt, turn_motor=turn_motor, power_motor=power_motor, turn_2 = turn_2, turn_3 = turn_3)

# define MechController
#mc = MechController()

# define DriverStation
ds = DriverStation.getInstance()





