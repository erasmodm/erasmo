# geometric_shape.py

from abc import ABC, abstractmethod

class GeometricShape(ABC):
    @abstractmethod
    def area(self):
        pass
