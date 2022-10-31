import os
import time
import curses
from threading import Thread
from PIL import Image, ImageDraw, ImageFont
from modules.general import *
from modules.widgets import *
from display.display_waveshare import *
from configuration import Configuration
from modules.renderer import Renderer
from modules.modules_manager import ModuleManager
from modules.mod_main.mod_main import ModuleMainView
from modules.coordinator import MainViewCoordinator

# Configuration
configuration: Configuration
modulesManager: ModuleManager
displayDevice: DisplayDeviceInterface
renderer: Renderer
viewCoordinator: MainViewCoordinator

def setup():
    """Setup the application, load configuration files, etc."""
    global configuration
    global modulesManager
    global renderer
    global displayDevice
    global viewCoordinator

    configuration = Configuration("config.yml")

    displayDevice = DisplayWaveshare()

    renderer = Renderer(
        width=configuration.screen["width"], 
        height=configuration.screen["height"], 
        background=ColorList.get_color("White"),
        displayDevice=displayDevice
        )

    viewCoordinator = MainViewCoordinator()
    viewCoordinator.setup(
        configuration=configuration,
        renderer=renderer
    )

    modulesManager = ModuleManager()
    modulesManager.load_modules()
    modulesManager.register_renderer(renderer=renderer)
    modulesManager.setup_modules(configuration=configuration)

    pass

def prepare_screen():
    global displayDevice
    displayDevice.setup()
    displayDevice.init()
    pass

def shutdown_screen():
    global displayDevice
    displayDevice.clear()
    displayDevice.deinit()
    pass

def draw():
    # view = ModuleMainView()
    # view.setup(renderer=renderer, viewCoordinator=viewCoordinator)
    # view.draw(renderer.image, renderer.draw)

    # displayDevice.clear()
    # displayDevice.display_full(renderer.image)
    #renderer.image.show()
    pass


def threaded():
    while 1:
        time.sleep(0.3)
        print('This is from another thread')
    pass

def main(win):
    """The main event queue"""
    thread = Thread(target=threaded)
    #thread.start()

    win.nodelay(True)
    key=""
    win.clear()                
    win.addstr("Detected key:")

    setup()
    prepare_screen()
    # draw()

    viewCoordinator.show_main_view()

    while 1:         
        time.sleep(1/60)
        print("Wait\r")
        try:                 
           key = win.getkey()         
           win.clear()                
           win.addstr("Detected key:")
           win.addstr(str(key)) 
           if key == os.linesep:
              break           
        except Exception as e:
           # No input   
           pass         

def main2():
    thread = Thread(target=threaded)
    thread.start()

    while 1:
        print("From main thread\n")
        time.sleep(0.3)
        pass
    pass

# main2()

curses.wrapper(main)



#time.sleep(2)
shutdown_screen()
