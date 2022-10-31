from ..modules_interfaces import *
from ..modules_manager import ModuleManager
from ..widgets import TextWidget, ViewInterface
from ..general import *
from threading import Thread
from threading import Timer
import time

class ModuleMain(ModuleInterface):

    # ModuleInterface

    def setup(self, configuration):
        super().setup(configuration)
        pass

    # ModuleWeather

    def __repr__(self):
        return 'ModuleMain!'

    pass # ModuleMain

class ModuleMainView(ViewInterface):
    __textWidget: TextWidget
    __text: str
    __index: int

    # ViewInterface

    def setup(self, renderer: RendererInterface, viewCoordinator: ViewCoordinator, configuration):
        super().setup(renderer=renderer, viewCoordinator=viewCoordinator, configuration=configuration)
        self.__setup()
        pass

    def draw(self, image, draw):
        self.__draw(image, draw)
        pass

    def will_deactivate(self):
        super().will_deactivate()
        self.__endTimer()
        
    def did_deactivate(self):
        return super().did_deactivate()

    def will_activate(self):
        return super().will_activate()

    def did_activate(self):
        super().did_activate()
        self.__redraw()
        self.renderer.enqueue_refresh(
            refresh=RendererInterface.RefreshRequest(frame=None)
        )
        self.__startTimer()

    # ModuleMainView

    def __repr__(self):
        return 'ModuleMainView!'

    def __setup(self):
        self.__textWidget = TextWidget()
        self.__textWidget.set_bounds(Rect(100, 100, 400, 200))
        self.__textWidget.set_font(
            FontList.get_font("Default").create(24)
        )
        self.__textWidget.set_text_color(
            ColorList.get_color("Black").rgb
        )
        self.__text = "111 ęśćLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"
        self.__index = 0

        pass

    def __draw(self, image, draw):
        self.__textWidget.draw(draw)
        pass

    def __startTimer(self):
        self.__timer = Timer(5.0, self.__fireTimer)
        self.__timer.start()
        pass

    def __endTimer(self):
        if self.__timer is not None:
            self.__timer.cancel()
            pass
        pass

    def __fireTimer(self):
        print("Timer fired\r")
        self.__textWidget.set_text(self.__text[:self.__index])
        self.__index += 1
        self.__redraw()
        # self.set_needs_update(True)
        #self.renderer.enqueue_refresh(RendererInterface.RefreshRequest(frame=None))
        self.renderer.enqueue_refresh(RendererInterface.RefreshRequest(frame=self.__textWidget.bounds))

        if self.is_active:
            self.__startTimer()
            pass
        pass

    def __redraw(self):
        self.draw(self.renderer.image, self.renderer.draw)
        pass

    pass # ModuleMainView
