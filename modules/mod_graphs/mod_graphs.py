from time import sleep, time
from ..modules_interfaces import ModuleInterface, WidgetInterface
from ..modules_manager import ModuleManager
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import numpy as np

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

    __figure: plt.Figure = None
    __ax = None

    # WidgetInterfaces

    def __init__(self) -> None:
        super().__init__()
        plt.style.use('_mpl-gallery')
        self.__fig, self.__ax = plt.subplots()
        pass

    def draw(self, image: Image, drawObject):
        plt.style.use('_mpl-gallery')
        bounds = self.bounds

        plt.gcf().set_size_inches(10, 5)

        # make data
        x = np.linspace(0, 20, 100)
        y = x#4 + 2 * np.sin(2 * x)

        # fig, ax = plt.subplots()
        self.__ax.plot(x, y, linewidth=2.0)
        self.__ax.set(
            xlim=(0, 8), xticks=np.arange(1, 8),
            ylim=(0, 8), yticks=np.arange(1, 8)
        )
        
        plot_image = self.fig2img(self.__fig, dpi=72)
        
        image.paste(plot_image, self.bounds.origin)
        pass

    def fig2img(self, fig: plt.Figure, dpi: int):
        """Convert a Matplotlib figure to a PIL Image and return it"""
        import io
        buf = io.BytesIO()
        fig.savefig(buf, dpi=dpi)
        buf.seek(0)
        img = Image.open(buf)
        return img

    pass #GraphWidget