from . import MacroSequence
from grt.core import Constants, GRTMacro
from grt.macro.blue_shoot_macro import BlueShootMacro

class BlueShootAuto(MacroSequence):
    """
    Basic autonomous mode. Drives and shoots. Pretty straightforward.
    """

    def __init__(self, swerve, shooter, intake):

        self.blue_shoot_macro = BlueShootMacro(swerve, shooter, intake)
        # c = Constants()
        # self.drive_macro = DriveMacro(dt, c['1balldrivedist'], c['1balldmtimeout'])
        # self.extend_macro = ExtendMacro(intake, 1.5)
        # self.wait_macro = GRTMacro(1.5)  # blank macro just waits
        # self.shoot_macro = ShootMacro(shooter, intake, 0.5)
        # self.wind_macro = WindMacro(shooter)
        self.macros = [self.blue_shoot_macro]
        super().__init__(macros=self.macros)
#         c.add_listener(self._constants_listener)

#     def _constants_listener(self, sensor, state_id, datum):
#         if state_id == '1balldrivedist':
#             self.drive_macro.distance = datum
#         elif state_id == '1balldmtimeout':
#             self.drive_macro.timeout = datum
# Contact GitHub API Training Shop Blog About