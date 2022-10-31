from turtle import back
from modules.general import Color
from modules.modules_interfaces import *
from PIL import Image, ImageDraw, ImageFont

class Renderer(RendererInterface):
    __image: Image

    def __init__(self, width: int, height: int, background: Color, displayDevice: DisplayDeviceInterface):
        self.__queue = []
        self.__image = Image.new(
            "RGB", (width, height), color=background.rgb
        )
        self.__draw = ImageDraw.Draw(self.__image)
        self.__draw.fontmode = "1" # disable aliasing
        self.__display = displayDevice
        pass

    @property
    def image(self):
        return self.__image

    @property
    def draw(self):
        return self.__draw

    @property
    def display(self):
        return self.__display

    def prepare(self):
        super().prepare()
        self.display.clear()            

    def enqueue_refresh(self, refresh: RendererInterface.RefreshRequest):
        super().enqueue_refresh(refresh=refresh)
        self.__push(item=refresh)
        pass

    def dequeue_refresh(self):
        super().dequeue_refresh()

        if self.__hasFullscreen:
            self.__render(item=RendererInterface.RefreshRequest(frame=None))
            self.__queue = []
            pass
        else:
            item = self.__pop()
            self.__render(item=item)
            return item
        
        pass

    def __push(self, item: RendererInterface.RefreshRequest):
        self.__queue.append(item)

    def __pop(self) -> RendererInterface.RefreshRequest:
        if len(self.__queue) > 0:
            item = self.__queue.pop()
            return item
        else:
            return None

    def __render(self, item: RendererInterface.RefreshRequest):
        if item is not None:
            self.display.pre_display()
            frame = item.frame
            if frame is not None:
                print("Render partial\r")
                self.display.display_partial(self.image, bounds=frame)
            else:
                print("Render full\r")
                self.display.display_full(self.image)
        pass

    @property
    def __hasFullscreen(self):
        for request in self.__queue:
            if request.is_fullscreen:
                return True
            pass
        return False

    pass # Renderer