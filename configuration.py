import yaml
from modules.general import FontList
from modules.general import ColorList

class Configuration:
    dict = {}

    def __init__(self, filename):

        with open(filename, "r") as stream:
            try:
                self._dict = yaml.safe_load(stream)
                FontList.from_config(self.fonts)
                ColorList.from_config(self.colors)
            except yaml.YAMLError as exc:
                print(exc)
        pass

    @property
    def raw(self):
        return self._dict

    @property
    def screen(self):
        return self._dict["screen"]

    @property
    def fonts(self):
        return self._dict["fonts"]

    @property
    def colors(self):
        return self._dict["colors"]

    pass # Configuration