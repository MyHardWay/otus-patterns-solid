import unittest
from random import random
from math import isclose

from numpy import array, ndarray, allclose
from numpy.linalg import norm
from tanks.commands.rotate import RotateCommand
from tanks.interfaces.rotable import IRotable
from tanks.commands.factory import RotateCommandFactory


class TestRotable(IRotable):
    def __init__(self) -> None:
        self.direction = array([random(), random(), random()])
        self.angular_velocity = array([random(), random(), random()])

    def get_direction(self) -> ndarray:
        return self.direction

    def get_angular_velocity(self) -> ndarray:
        return self.angular_velocity

    def set_direction(self, new_direction: ndarray) -> None:
        self.direction = new_direction


class TestRotateCommand:
    def __init__(self, obj: IRotable) -> None:
        self.obj = obj

    def __call__(self) -> None:
        command = RotateCommand(self.obj)
        command()


class TestRotateWithFactory(unittest.TestCase):
    def test_set_get_command(self):
        factory = RotateCommandFactory()
        factory.set_command(TestRotable, TestRotateCommand)
        rotable = TestRotable()
        collinear_to_new_direction = rotable.get_direction() + rotable.get_angular_velocity()
        command = factory.get_command(rotable)

        command()

        ratio = norm(rotable.get_direction()) / norm(collinear_to_new_direction)
        self.assertTrue(allclose(collinear_to_new_direction * ratio, rotable.get_direction()))
        self.assertTrue(isclose(norm(rotable.get_direction()), 1))

if __name__ == "__main__":
    unittest.main()
