from IT8951.display import AutoEPDDisplay
from IT8951.display import EPD
from IT8951 import constants
from IT8951 import img_manip

from modules.modules_interfaces import *
import logging

class DisplayWaveshare(DisplayDeviceInterface):
    """Concrete class for the e-ink Waveshare device."""

    __display_mode = constants.DisplayModes.GC16
    
    def __init__(self):
        self.__logger = logging.getLogger('DisplayWaveshare')

    def setup(self, configuration):
        super().setup(configuration)
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
        """"
        Clear display, device image buffer, and frame buffer (e.g. at startup)
        """
        super().clear()
        self.__logger.debug("Clear")
        self.__display.clear()

    def sleep(self):
        super().sleep()
        self.__epd.sleep()

    def display_full(self, image: Image):
        super().display_full(image)

        self.__logger.debug("Display full")
        frame = image
        display_dims = [image.width, image.height]
        self.__display.update(frame.tobytes(), (0,0), display_dims, self.__display_mode, pixel_format=constants.PixelModes.M_8BPP) #M_8BPP = 3
        pass

    def display_partial(self, image: Image, bounds: Rect):
        super().display_partial(image, bounds)
        self.__logger.info("Display partial; (x,y)=%s", bounds)
        
        mod_image = image.crop(bounds.shape)

        self.__display.update(
            data=mod_image.tobytes(), 
            xy=bounds.origin, 
            dims=bounds.size, 
            mode=constants.DisplayModes.DU, 
            pixel_format=constants.PixelModes.M_8BPP
        )

        # self.__display.update(
        #     data=image.tobytes(), 
        #     xy=(bounds.x, bounds.y), 
        #     dims=(bounds.width, bounds.height), 
        #     mode=constants.DisplayModes.DU, 
        #     pixel_format=constants.PixelModes.M_8BPP
        # )

    pass # DisplayWaveshare