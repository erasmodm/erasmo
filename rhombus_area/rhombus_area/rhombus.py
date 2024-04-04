# rhombus.py

from geometric_shape import GeometricShape

class Rhombus(GeometricShape):
    def __init__(self, major_diagonal, minor_diagonal):
        self.major_diagonal = major_diagonal
        self.minor_diagonal = minor_diagonal

    def area(self):
        return (self.major_diagonal * self.minor_diagonal) / 2
