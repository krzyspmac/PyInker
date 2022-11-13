import os
import time
import curses
from threading import Thread
from PIL import Image, ImageDraw, ImageFont
from modules.general import *
from modules.widgets import *
# from display.display_waveshare import *
from display.display_dummy import *
from configuration import Configuration
from modules.renderer import Renderer
from modules.modules_manager import ModuleManager
from modules.mod_main.mod_main import ModuleMainView
from modules.coordinator import MainViewCoordinator
import logging

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

    logger_file = configuration.base["logger_file"] or "output.log"
    logging.basicConfig(
        filename=logger_file,
        format='%(asctime)s %(name)20s - %(funcName)20s() %(message)s',
        level=logging.INFO
        )
    # logging.basicConfig(format='%(asctime)s %(name)s -- %(funcName)s %(message)s')
    logging.info("Booting system...")

    logging.info("Booting Display Driver...")
    if configuration.display_driver["is_dummy"] is True:
        displayDevice = DisplayDummy()
    else:
        displayDevice = DisplayWaveshare()
        pass

    logging.info("Booting Renderer...")
    renderer = Renderer(
        width=configuration.screen["width"], 
        height=configuration.screen["height"], 
        background=ColorList.get_color("White"),
        displayDevice=displayDevice
        )

    logging.info("Booting View Coordinator...")
    viewCoordinator = MainViewCoordinator()
    viewCoordinator.setup(
        configuration=configuration,
        renderer=renderer
    )

    logging.info("Booting Module Manager")
    modulesManager = ModuleManager()
    modulesManager.load_modules()
    modulesManager.register_renderer(renderer=renderer)
    modulesManager.setup_modules(configuration=configuration)

    pass

def prepare_screen():
    global displayDevice
    global configuration
    global renderer

    logging.info("Preparing Screen...")
    displayDevice.setup(
        configuration=configuration,
        image=renderer.image
    )
    displayDevice.init()
    pass

def shutdown_screen():
    global displayDevice

    logging.info("Shutting off the screen...")
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
    viewCoordinator.show_main_view()

    renderer.prepare()

    while 1:         
        time.sleep(10/60)
        print("Wait\r")

        while renderer.dequeue_refresh() is not None:
            print("Rendering...\r")
            pass

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
viewCoordinator.deinit()
