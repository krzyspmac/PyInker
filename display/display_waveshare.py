from modules.modules_interfaces import *
import sys
import os

libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_epd import epd7in5_V2

class DisplayWaveshare(DisplayDeviceInterface):
    """Concrete class for the e-ink Waveshare device."""
    
    def setup(self):
        super().setup()
        self.__epd = epd7in5_V2.EPD()

    def init(self):
        super().init()
        self.__epd.init()

    def deinit(self):
        super().deinit()
        epd7in5_V2.epdconfig.module_exit()

    def clear(self):
        super().clear()
        self.__epd.Clear()

    def sleep(self):
        super().sleep()
        self.__epd.sleep()

    def display_full(self, image: Image):
        super().display_full(image)
        self.__epd.display(self.__epd.getbuffer(image))

    def display_partial(self, image: Image, bounds: Rect):
        # Not supported yet
        super().display_partial(image, bounds)
        self.__epd.display(self.__epd.getbuffer(image))

    pass # DisplayWaveshare