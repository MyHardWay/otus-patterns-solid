import unittest

from tanks.commands.factory import RotateCommandFactory
from tanks.interfaces.physical_object import PhysicalObject


class TestObject(PhysicalObject):
    pass


class TestCommand(object):
    def __init__(self, obj: PhysicalObject):
        pass

    def __exec__(self):
        pass


class TestRotateCommandFactory(unittest.TestCase):
    def test_set_get_command(self):
        factory = RotateCommandFactory()
        factory.set_command(TestObject, TestCommand)
        test_object = TestObject()

        test_command = factory.get_command(test_object)

        self.assertIsInstance(test_command, TestCommand)

if __name__ == "__main__":
    unittest.main()
