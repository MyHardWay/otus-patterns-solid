import unittest
from random import random

from numpy import array, ndarray, allclose
from tanks.commands.linear_move import LinearMoveCommand
from tanks.interfaces.movable import IMovable
from tanks.commands.factory import MoveCommandFactory


class TestMovable(IMovable):
    def __init__(self) -> None:
        self.position = array([random(), random(), random()])
        self.velocity = array([random(), random(), random()])

    def get_position(self) -> ndarray:
        return self.position

    def get_velocity(self) -> ndarray:
        return self.velocity

    def set_position(self, new_position) -> None:
        self.position = new_position


class TestMoveCommand:
    def __init__(self, obj: IMovable) -> None:
        self.obj = obj

    def __call__(self) -> None:
        command = LinearMoveCommand(self.obj)
        command()


class TestMoveFromFactory(unittest.TestCase):
    def test_set_get_command(self):
        factory = MoveCommandFactory()
        factory.set_command(TestMovable, TestMoveCommand)
        movable = TestMovable()
        expected_result = movable.get_position() + movable.get_velocity()
        command = factory.get_command(movable)

        command()

        self.assertTrue(allclose(movable.get_position(), expected_result))

if __name__ == "__main__":
    unittest.main()
