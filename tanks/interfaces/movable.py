from abc import ABC, abstractmethod
from numpy import ndarray

from tanks.interfaces.physical_object import PhysicalObject


class IMovable(ABC):
    """Movable object interface
    """
    @abstractmethod
    def get_position(self) -> ndarray:
        pass

    @abstractmethod
    def set_position(self, new_position: ndarray) -> None:
        pass

    @abstractmethod
    def get_velocity(self) -> ndarray:
        pass


class MovableAdapter(IMovable):
    """Atapts a physical objects to the :class:`IMovable` interface
    """
    __slots__ = ("_object",)

    def __init__(self, obj: PhysicalObject) -> None:
        self._object = obj

    def get_position(self) -> ndarray:
        return self._object.__getattr__("position")

    def set_position(self, new_position: ndarray) -> None:
        self._object.__setattr__("position", new_position)

    def get_velocity(self) -> ndarray:
        return self._object.__getattr__("velocity")
