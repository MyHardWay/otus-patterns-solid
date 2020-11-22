import unittest

from numpy import array
from tanks.interfaces.rotable import RotableAdapter
from tanks.interfaces.physical_object import PhysicalObject


class TestPhysicalObject(PhysicalObject):
    pass


class TestRotableAdapter(unittest.TestCase):
    def test_get_direction(self):
        direction = array([])
        physical_object = TestPhysicalObject(direction=direction)
        adapter = RotableAdapter(physical_object)

        object_direction = adapter.get_direction()

        self.assertIs(direction, object_direction)

    def test_get_angular_velocity(self):
        angular_velocity = array([])
        physical_object = TestPhysicalObject(angular_velocity=angular_velocity)
        adapter = RotableAdapter(physical_object)

        object_angular_velocity = adapter.get_angular_velocity()

        self.assertIs(angular_velocity, object_angular_velocity)

    def test_set_direction(self):
        direction = array([])
        physical_object = TestPhysicalObject()
        adapter = RotableAdapter(physical_object)

        adapter.set_direction(direction)

        self.assertIs(direction, adapter.get_direction())

if __name__ == "__main__":
    unittest.main()
