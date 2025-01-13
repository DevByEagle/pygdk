from typing import Union, Tuple, Sequence

Coordinate = Union[Tuple[float, float], Sequence[float], Vector2]

class Vector2:
    x: int
    y: int
    def __init__(self, x: int, y: int): ...
