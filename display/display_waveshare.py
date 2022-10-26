from modules.modules_interfaces import *
import sys
import os

libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_epd import epd7in5_V2

class DisplayWaveshare(DisplayDeviceInterface):
    """Concrete class for the e-ink Waveshare device."""
    
    pass # DisplayWaveshare