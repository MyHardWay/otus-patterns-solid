from tanks.interfaces.movable import IMovable


class LinearMoveCommand(object):
    """Linear move of physical object
    """
    __slots__ = ("_movable",)

    def __init__(self, movable: IMovable):
        self._movable = movable

    def __call__(self):
        self._movable.set_position(self._movable.get_position() + self._movable.get_velocity())
