from tanks.interfaces.rotable import IRotable

from numpy.linalg import norm


class RotateCommand(object):
    """Rotation of phyical object
    """
    __slots__ = ("_rotable",)

    def __init__(self, rotable: IRotable):
        self._rotable = rotable

    def __call__(self):
        direction_vector = self._rotable.get_direction() + self._rotable.get_angular_velocity()
        self._rotable.set_direction(direction_vector/norm(direction_vector))
