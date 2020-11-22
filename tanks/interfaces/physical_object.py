from abc import ABC


class PhysicalObject(ABC):
    """Universal interface for physical objects
    """
    __slots__ = ("__dict__",)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__dict__[key] = value

    def __getattr__(self, attr: str):
        return self.__dict__[attr]

    def __setattr__(self, attr: str, value):
        self.__dict__[attr] = value
