import unittest

from numpy import array
from tanks.interfaces.movable import MovableAdapter
from tanks.interfaces.physical_object import PhysicalObject


class TestPhysicalObject(PhysicalObject):
    pass


class TestMovableAdapter(unittest.TestCase):
    def test_get_position(self):
        position = array([])
        physical_object = TestPhysicalObject(position=position)
        adapter = MovableAdapter(physical_object)

        object_position = adapter.get_position()

        self.assertIs(position, object_position)

    def test_get_velocity(self):
        velocity = array([])
        physical_object = TestPhysicalObject(velocity=velocity)
        adapter = MovableAdapter(physical_object)

        object_velocity = adapter.get_velocity()

        self.assertIs(velocity, object_velocity)

    def test_set_position(self):
        position = array([])
        physical_object = TestPhysicalObject()
        adapter = MovableAdapter(physical_object)

        adapter.set_position(position)

        self.assertIs(position, adapter.get_position())

if __name__ == "__main__":
    unittest.main()
