from abc import ABC, abstractmethod
from numpy import ndarray

from tanks.interfaces.physical_object import PhysicalObject


class IRotable(ABC):
    """Rotable object interface
    """
    @abstractmethod
    def get_direction(self) -> ndarray:
        pass

    @abstractmethod
    def set_direction(self, value: ndarray) -> None:
        pass

    @abstractmethod
    def get_angular_velocity(self) -> ndarray:
        pass


class RotableAdapter(IRotable):
    """Atapts a physical objects to the :class:`IRotable` interface
    """
    __slots__ = ("_object",)

    def __init__(self, obj: PhysicalObject):
        self._object = obj

    def get_direction(self) -> ndarray:
        return self._object.__getattr__("direction")

    def set_direction(self, new_direction: ndarray) -> None:
        self._object.__setattr__("direction", new_direction)

    def get_angular_velocity(self) -> ndarray:
        return self._object.__getattr__("angular_velocity")
