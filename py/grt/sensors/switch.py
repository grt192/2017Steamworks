__author__ = "Calvin Huang"

import time
try:
    from wpilib import DigitalInput
except ImportError:
    from pyfrc.wpilib import DigitalInput

from grt.core import Sensor


class Switch(Sensor):
    """
    Sensor wrapper for a switch.

    Has boolean attribute pressed.
    """

    def __init__(self, channel, module=1, reverse=False):
        """
        Initializes the switch on some digital channel and module.
        Normally assumes switches are active low.
        """
        super().__init__()
        self.s = DigitalInput(channel)
        self.reverse = reverse
        self.time = 0.0
        self.pressed = False
        
    def isPressed(self):
        return self.pressed
    
    def poll(self):
        button_pressed_at_this_moment = not self.s.get() ^ self.reverse
        if button_pressed_at_this_moment != self.pressed and (time.time() - self.time) >= 0.100:
            self.pressed = button_pressed_at_this_moment
            self.time = time.time()
