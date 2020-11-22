from abc import ABC, abstractmethod
from typing import Callable

from tanks.interfaces.physical_object import PhysicalObject
from tanks.interfaces.movable import IMovable
from tanks.interfaces.rotable import IRotable


class CommandFactory(ABC):
    """Abstract command factory class
    """
    __slots__ = ("__dict__",)

    @abstractmethod
    def get_command(self, obj: PhysicalObject) -> Callable:
        pass
    
    @abstractmethod
    def set_command(self, obj_class: type, command_class: type) -> None:
        pass


class MoveCommandFactory(CommandFactory):
    """Move command factory class
    """
    def get_command(self, obj: IMovable) -> Callable:
        return self.__dict__[type(obj)](obj)
    
    def set_command(self, obj_class: type, command_class: type) -> None:
        self.__dict__[obj_class] = command_class


class RotateCommandFactory(CommandFactory):
    """Rotate command factory class
    """
    def get_command(self, obj: IRotable) -> Callable:
        return self.__dict__[type(obj)](obj)

    def set_command(self, obj_class: type, command_class: type) -> None:
        self.__dict__[obj_class] = command_class
