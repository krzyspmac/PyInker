from IT8951.display import AutoEPDDisplay
from IT8951.display import EPD
from IT8951 import constants
from IT8951 import img_manip

from modules.modules_interfaces import *
import logging

class DisplayWaveshare(DisplayDeviceInterface):
    """Concrete class for the e-ink Waveshare device."""
    
    def __init__(self):
        self.__logger = logging.getLogger('DisplayWaveshare')

    def setup(self, configuration, image: Image):
        super().setup(configuration, image)
        self.__logger.info("Setting IT8951 display")
        self.__voltage = configuration.raw["display_driver"]["epd_voltage"]
        pass

    def init(self):
        super().init()
        self.__logger.info("Initializing IT8951 display; voltage=" + str(self.__voltage))
        self.__display = AutoEPDDisplay(vcom=self.__voltage)
        self.__epd = self.__display.epd
        self.__logger.info("screen width=" + str(self.__epd.width))
        self.__logger.info("screen height=" + str(self.__epd.height))
        pass

    def deinit(self):
        super().deinit()
        self.__logger.info("Deinitializing IT8951")
        self.__epd.sleep()
        pass

    def clear(self):
        super().clear()
        self.__logger.debug("Clear")
        self.__display.clear()

    def sleep(self):
        super().sleep()
        self.__epd.sleep()

    def display_full(self, image: Image):
        super().display_full(image)

        self.__logger.debug("Display full")
        self.__display.update(
            data=image.tobytes(), 
            xy=(0,0), 
            dims=[image.width, image.height], 
            mode=constants.DisplayModes.GC16, 
            pixel_format=constants.PixelModes.M_8BPP
        )
        pass

    def display_partial(self, image: Image, bounds: Rect):
        super().display_partial(image, bounds)
        self.__logger.info("Display partial; (x,y)=%s", bounds)

        self.__display.update(
            data=image.crop(bounds.shape).tobytes(), 
            xy=bounds.origin, 
            dims=bounds.size, 
            mode=constants.DisplayModes.DU, 
            pixel_format=constants.PixelModes.M_8BPP
        )
        pass

    def display_partial_computed(self, image: Image):
        self.__logger.error("Not supported")
        pass

    pass # DisplayWaveshare