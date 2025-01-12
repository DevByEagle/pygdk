class Vector2:
    def __init__(self, x=0.0, y=0.0):
        if not isinstance(x, (int, float)):
            raise TypeError(f"x must be a float or int, not {type(x).__name__}")
        if not isinstance(y, (int, float)):
            raise TypeError(f"y must be a float or int, not {type(y).__name__}")
        self.x = float(x)
        self.y = float(y)
    
    def __getitem__(self, index: int) -> float:
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Index out of range. Use 0 for x or 1 for y.")
    
    def __setitem__(self, index, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Value must be a float or int, not {type(value).__name__}")
        if index == 0:
            self.x = float(value)
        elif index == 1:
            self.y = float(value)
        else:
            raise IndexError("Index out of range. Use 0 for x or 1 for y.")
    def __add__(self, other: "Vector2") -> "Vector2":
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        raise TypeError(f"Unsupported operand type(s) for +: 'Vector2' and '{type(other).__name__}'")

    def __sub__(self, other: "Vector2") -> "Vector2":
        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        raise TypeError(f"Unsupported operand type(s) for -: 'Vector2' and '{type(other).__name__}'")

    def __mul__(self, scalar: float) -> "Vector2":
        if isinstance(scalar, (int, float)):
            return Vector2(self.x * scalar, self.y * scalar)
        raise TypeError(f"Unsupported operand type(s) for *: 'Vector2' and '{type(scalar).__name__}'")

    def __truediv__(self, scalar: float) -> "Vector2":
        if isinstance(scalar, (int, float)):
            if scalar == 0:
                raise ZeroDivisionError("division by zero")
            return Vector2(self.x / scalar, self.y / scalar)
        raise TypeError(f"Unsupported operand type(s) for /: 'Vector2' and '{type(scalar).__name__}'")

    def __eq__(self, other: "Vector2") -> bool:
        return isinstance(other, Vector2) and self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Vector2({self.x}, {self.y})"

    def dot(self, other):
        if isinstance(other, Vector2):
            return self.x * other.x + self.y * other.y
        raise TypeError(f"Dot product requires another Vector2, not {type(other).__name__}")
