from .modules_interfaces import ViewCoordinator, ViewInterface
from .modules_interfaces import RendererInterface
from .mod_main.mod_main import ModuleMainView

class MainViewCoordinator(ViewCoordinator):
    __activeView: ViewInterface = None

    def setup(self, configuration, renderer: RendererInterface):
        super().setup(configuration, renderer=renderer)
        self.__renderer = renderer

        self.__mainView = ModuleMainView()
        self.main_view.setup(
            renderer=self.renderer,
            viewCoordinator=self,
            configuration=configuration
        )
        pass

    def deinit(self):
        super().deinit()
        self.__activeView.will_activate()
        self.__activeView.did_deactivate()
        pass

    def set_view_active(self, view: ViewInterface):
        super().set_view_active(view)
        lastView = self.__activeView

        if lastView is not None:
            lastView.will_deactivate()
            pass

        view.will_activate()

        if lastView is not None:
            lastView.did_deactivate()
            pass

        view.did_activate()
        self.__activeView = view

    def show_main_view(self):
        self.set_view_active(self.__mainView)
        pass

    def frame_update(self):
        super().frame_update()
        if self.active_view is not None:
            if self.active_view.needs_update:
                self.active_view.draw(self.renderer.image, self.renderer.draw)
                self.active_view.set_needs_update(False)
                pass
            pass
        pass

    @property
    def active_view(self):
        return self.__activeView

    @property
    def renderer(self):
        return self.__renderer

    @property
    def main_view(self):
        return self.__mainView

    pass
