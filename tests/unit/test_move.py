import unittest
from random import random

from numpy import array, ndarray, allclose
from tanks.commands.linear_move import LinearMoveCommand
from tanks.interfaces.movable import IMovable


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


class TestLinearMove(unittest.TestCase):
    def test_linear_move(self):
        """Tests if the linear move command moves an object correctly
        """
        movable = TestMovable()
        expected_result = movable.get_position() + movable.get_velocity()
        command = LinearMoveCommand(movable)
        
        command()
        
        self.assertTrue(allclose(movable.get_position(), expected_result))

if __name__ == "__main__":
    unittest.main()
