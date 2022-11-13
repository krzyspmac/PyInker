from locale import YESEXPR
from time import sleep, time
from ..modules_interfaces import ModuleInterface, WidgetInterface
from ..modules_manager import ModuleManager
from PIL import Image, ImageDraw, ImageFont
import logging
from logging import LoggerAdapter
import matplotlib.pyplot as plt
import numpy as np
import math

class ModuleGraphs(ModuleInterface):

    # ModuleInterface

    def setup(self, configuration):
        super().setup(configuration)
        pass

    # ModuleWidgets

    def __repr__(self):
        return 'ModuleGraphs!'

    pass # ModuleGraphs

class GraphWidget(WidgetInterface):
    """Draws x,y graph. The simplest of the kind."""

    __logger: LoggerAdapter
    __figure: plt.Figure = None
    __ax = None
    __dpi = 72

    __data_x = [0,  1,  2,  3, 4,  5]
    __data_y = [25, 20, 15, 5, 17, 0]

    y_step = 10                         # control the step for ticks
    line_width: float                   # control the line width
    main_title_font_size: float         # control the main title font-size
    tick_font_size: float               # control the font-size of tick values
    title_font_size: float              # control the font-size of titles
    x_axis_label: str = None            # control the x-axis title label
    y_axis_label: str = None            # control the y-axis title label
    title_label: str = None             # control the title of the graph

    def setup(
            self, 
            line_width: float = 2.0,
            y_step: float = 10,
            dpi: float = 72.0,
            main_title_font_size: float = 20.0,
            title_font_size: float = 20.0,
            tick_font_size: float = 15.0
        ):
        """Setup visual appearance."""
        self.line_width = line_width
        self.y_step = y_step
        self.__dpi = dpi
        self.main_title_font_size = main_title_font_size
        self.title_font_size = title_font_size
        self.tick_font_size = tick_font_size
        pass
    
    def set_data(
            self, 
            x_data, 
            y_data, 
            title_label: str = "Temparature",
            x_axis_label: str = None,
            y_axis_label: str = None
        ):
        """Set the data. Provide two equal arrays of floating point values."""
        self.__data_x = x_data
        self.__data_y = y_data
        self.title_label = title_label
        self.x_axis_label = None
        self.y_axis_label = None
        pass

    # WidgetInterfaces

    def __init__(self) -> None:
        super().__init__()
        self.setup()
        self.__logger = logging.getLogger('ModuleGraphs')
        plt.style.use('_mpl-gallery')
        self.__fig, self.__ax = plt.subplots()
        pass

    def draw(self, image: Image, drawObject):
        plt.style.use('_mpl-gallery')
        bounds = self.bounds

        # plt.gcf().set_size_inches(10, 5)
        plt.gcf().set_size_inches(
            math.floor(self.bounds.width / self.__dpi),
            math.floor(self.bounds.height / self.__dpi),
        )
        xmin, xmax = self.__xaxis_limits()
        ymin, ymax = self.__yaxis_limits()        
        ymin_display = math.floor( ((ymin/self.y_step) - 1) * self.y_step )
        ymax_display = math.floor( ((ymax/self.y_step) + 1) * self.y_step )

        x_ticks = np.arange(xmin + 1, xmax)
        y_ticks = np.arange(ymin_display, ymax_display, self.y_step)

        self.__ax.plot(self.__data_x, self.__data_y, linewidth=self.line_width)
        self.__ax.set(
            xlim=(xmin, xmax), xticks=x_ticks,
            ylim=(ymin, ymax), yticks=y_ticks,
        )
        if self.x_axis_label is not None:
            self.__ax.set_xlabel(self.x_axis_label, fontsize=self.title_font_size)
            pass
        if self.y_axis_label is not None:
            self.__ax.set_ylabel(self.y_axis_label, fontsize=self.title_font_size)
            pass
        self.__ax.xaxis.label.set_fontsize(self.tick_font_size)
        self.__ax.yaxis.label.set_fontsize(self.tick_font_size)
        for label in self.__ax.get_xticklabels() + self.__ax.get_yticklabels():
            label.set_fontsize(self.tick_font_size)
            pass
        if self.title_label is not None:
            self.__ax.set_title(self.title_label, fontsize=self.main_title_font_size)
            pass
        
        plot_image = self.fig2img(self.__fig, dpi=self.__dpi)
        
        image.paste(plot_image, self.bounds.origin)
        pass

    def fig2img(self, fig: plt.Figure, dpi: int):
        """Convert a Matplotlib figure to a PIL Image and return it"""
        import io
        buf = io.BytesIO()
        fig.savefig(buf, dpi=dpi, bbox_inches='tight')
        buf.seek(0)
        img = Image.open(buf)
        return img

    def __xaxis_limits(self):
        return ( min(self.__data_x), max(self.__data_x) )

    def __yaxis_limits(self):
        return ( min(self.__data_y), max(self.__data_y) )

    pass #GraphWidget