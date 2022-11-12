import tkinter as tk
from PIL import ImageTk

from modules.modules_interfaces import *
import logging

class DisplayDummy(DisplayDeviceInterface):
    """Concrete class for the e-ink Waveshare device."""

    __dummy_filename: str = None

    def __init__(self):
        self.__logger = logging.getLogger('DisplayDummy')
        self.__root = tk.Tk()
        self.__photoimage = ImageTk.PhotoImage
        pass

    def setup(self, configuration, image: Image):
        super().setup(configuration, image)
        self.__logger.info("Setting dummy display")
        self.__dummy_filename = configuration.display_driver["dummy_file"]

        self.__pil_img = Image.new('L', (1400, 800), 0xFF) #image.copy()
        self.__tk_img = self.__photoimage(self.__pil_img)
        self.__panel = tk.Label(self.__root, image=self.__tk_img)
        self.__panel.pack(side="bottom", fill="both", expand="yes")
        pass

    def init(self):
        super().init()
        self.__logger.info("Initializing dummy display")
        pass

    def deinit(self):
        super().deinit()
        self.__logger.info("Deinitializing dummy display")
        pass

    def clear(self):
        super().clear()
        self.__logger.debug("Clear")

    def sleep(self):
        super().sleep()

    def display_full(self, image: Image):
        super().display_full(image)
        self.__logger.debug("Display full")
        self.__save(image)
        pass

    def display_partial(self, image: Image, bounds: Rect):
        super().display_partial(image, bounds)
        self.__logger.info("Display partial; (x,y)=%s", bounds)
        self.__save(image)
        pass

    def display_partial_computed(self, image: Image):
        self.__logger.error("Not supported")
        pass

    def __save(self, image: Image):
        image.save(self.__dummy_filename)
        pass

    pass # DisplayWaveshare