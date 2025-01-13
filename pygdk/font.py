class Font:
    def __init__(self, family="Arial", size=12, weight="normal"):
        self.family = family
        self.size = size
        self.weight = weight
    
    def get_font(self):
        return (self.family, self.size, self.weight)