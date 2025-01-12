class Color:
    r: int
    g: int
    b: int
    def __init__(self, r: int, g: int, b: int): ...

    @property
    def RGBName(self) -> str: ...