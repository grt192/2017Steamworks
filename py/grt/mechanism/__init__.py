from ctre import CANTalon

class ZeroTest:

    def __init__(self, motor, limit_switch):

        self.motor = motor

        self.limit_switch = limit_switch

        limit_switch.add_listener(self._limit_listener)

    def go(self, power):

        print("going!!")

        self.motor.changeControlMode(CANTalon.ControlMode.PercentVbus)



        # self.motor.set(power)

        if not self.limit_switch.pressed:

            print("if statement")

            self.motor.set(power)


    def _limit_listener(self, source, state_id, datum):

        if state_id == 'pressed' and datum:


            print("listener")

            self.motor.changeControlMode(CANTalon.ControlMode.PercentVbus)
            self.motor.set(0)

class TalonTester:

    def __init__(self, motor=None, pneumatic=None):

        self.pneumatic = pneumatic
        self.motor = motor

    def go_pneumatic(self, bool):
        print("going")

        self.pneumatic.set(bool)

    def go_motor(self, power):
        self.motor.set(power)


            