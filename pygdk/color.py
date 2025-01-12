import webcolors

class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    
    @property
    def RGBName(self):
        try:
            return webcolors.rgb_to_name((self.r, self.g, self.b))
        except ValueError:
            raise RuntimeWarning("Unknown color")