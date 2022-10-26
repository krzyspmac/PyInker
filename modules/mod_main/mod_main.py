from ..modules_interfaces import *
from ..modules_manager import ModuleManager
from ..widgets import TextWidget, ViewInterface
from ..general import *

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

    # ViewInterface

    def setup(self, renderer: RendererInterface):
        super().setup(renderer=renderer)
        self.__setup()
        pass

    def draw(self, image, draw):
        self.__draw(image, draw)
        pass

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
        pass

    def __draw(self, image, draw):
        self.__textWidget.set_text("111 ęśćLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum")
        self.__textWidget.draw(draw)
        pass

    pass # ModuleMainView
