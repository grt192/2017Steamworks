from wpilib import CANTalon

class MechController:

    def __init__(self, turn_motor, driver_joystick, xbox_controller, limit_switch=None): # mechanisms belong in arguments
        # define mechanisms here
        self.driver_joystick = driver_joystick
        self.xbox_controller = xbox_controller
        self.limit_switch = limit_switch
        self.turn_motor = turn_motor


        driver_joystick.add_listener(self._driver_joystick_listener)
        xbox_controller.add_listener(self._xbox_controller_listener)

    def _xbox_controller_listener(self, sensor, state_id, datum):
        if state_id == "a_button":
            if datum:
                self.turn_motor.changeControlMode(CANTalon.ControlMode.PercentVbus)
                self.turn_motor.set(.2)
 
                print(self.limit_switch.get())
                print(self.turn_motor.getEncPosition())
                #if self.limit_switch.get():
                #    self.turn_motor.setEncPosition(0)
                #    print("triggered")
            else:
                self.turn_motor.changeControlMode(CANTalon.ControlMode.PercentVbus)
                self.turn_motor.set(0)

    def _driver_joystick_listener(self, sensor, state_id, datum):
        pass

    def msryzhik(self):
        pass


