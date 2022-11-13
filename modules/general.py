from PIL import Image, ImageDraw, ImageFont

class Rect:
    @staticmethod
    def zero():
        return Rect(0, 0, 0, 0)

    def __init__(self, x: int, y: int, width: int, height: int):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        pass

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def origin(self):
        return (self.x, self.y)

    @property
    def size(self):
        return [self.width, self.height]

    @property
    def shape(self):
        return (self.x, self.y, self.x + self.width, self.y + self.height)

    def __repr__(self):
        return "(x=" + str(self.x) + ", y=" + str(self.y) + ", w=" + str(self.width) + ", h=" + str(self.height) + ")"

    pass # Rect

class FontList:
    fonts = { }

    @staticmethod
    def from_config(cfg):
        for font_descriptor in cfg:
            FontList.add_font(font_descriptor)
        pass

    @staticmethod
    def add_font(cfg):
        name = cfg["name"]
        FontList.fonts[name] = Font(name, cfg["path"])
        pass

    @staticmethod
    def get_font(name):
        return FontList.fonts[name]

    pass # FontList

class Font:
    def __init__(self, name: str, path):
        self._name = name
        self._path = path
        pass

    def create(self, size: int):
        return ImageFont.truetype(self._path, size)

    pass # Font

class ColorList:
    colors = { }

    @staticmethod
    def from_config(cfg):
        for color_descriptor in cfg:
            ColorList.add_color(color_descriptor)
        pass

    @staticmethod
    def add_color(cfg):
        name = cfg["name"]
        ColorList.colors[name] = Color(cfg["values"])
        pass

    @staticmethod
    def get_color(name):
        return ColorList.colors[name]

    pass # ColorList

class Color:

    def __init__(self, val):
        self.__val = val

    @property
    def grayscale(self):
        return self.__val

    pass # Color

def text_wrap(text,font,writing,max_width,max_height,max_lines=9999):
    lines = [[]]
    words = text.split()
    for word in words:
        # try putting this word in last line then measure
        lines[-1].append(word)
        (w,h) = writing.multiline_textsize('\n'.join([' '.join(line) for line in lines]), font=font)
        if w > max_width: # too wide
            # take it back out, put it on the next line, then measure again
            lines.append([lines[-1].pop()])
            (w,h) = writing.multiline_textsize('\n'.join([' '.join(line) for line in lines]), font=font)
            if h > max_height: # too high now, cannot fit this word in, so take out - add ellipses
                lines.pop()
                # try adding ellipses to last word fitting (i.e. without a space)
                lines[-1][-1] += '...'
                # keep checking that this doesn't make the textbox too wide, 
                # if so, cycle through previous words until the ellipses can fit
                while writing.multiline_textsize('\n'.join([' '.join(line) for line in lines]),font=font)[0] > max_width:
                    lines[-1].pop()
                    if lines[-1]:
                        lines[-1][-1] += '...'
                    else:
                        lines[-1].append('...')
                break
    return '\n'.join([' '.join(line) for line in lines])