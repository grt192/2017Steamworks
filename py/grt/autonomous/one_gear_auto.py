"""
basic_auto.py
"""



from . import MacroSequence
from grt.core import Constants, GRTMacro
from collections import OrderedDict
from grt.macro.gear_vision_macro import GearVisionMacro



class MiddleGear(MacroSequence):
    """
    Basic autonomous mode. Drives and shoots. Pretty straightforward.
    """

    def __init__(self, swerve,robot_vision, gear, timeout=None):

        self.gear_vision_macro = GearVisionMacro(swerve, shooter, intake)

        self.macros = [self.gear_vision_macro]
        super().__init__(macros=self.macros)

        