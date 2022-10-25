from turtle import back
from modules.general import Color
from modules.modules_interfaces import *
from PIL import Image, ImageDraw, ImageFont

class Renderer(RendererInterface):
    __image: Image

    def __init__(self, width: int, height: int, background: Color, displayDevice: DisplayDeviceInterface):
        self.__image = Image.new(
            "RGB", (width, height), color=background.rgb
        )
        self.__draw = ImageDraw.Draw(self.__image)
        pass

    @property
    def image(self):
        return self.__image

    @property
    def draw(self):
        return self.__draw

    def enqueue_refresh(self, refresh: RendererInterface.RefreshRequest):
        super().enqueue_refresh()
        pass

    def display(self):
        super().display()

    pass # Renderer