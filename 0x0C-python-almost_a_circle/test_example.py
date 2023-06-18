import unittest
import my_module


class MyModuleTestCase(unittest.TestCase):
    def test_get_name(self):
        my_object = my_module.MyClass("Alice")
        self.assertEqual(my_object.get_name(), "Alice")

    def test_greet(self):
        my_object = my_module.MyClass("Bob")
        self.assertEqual(my_object.greet(), "Hello, Bob!")

    def test_add_numbers(self):
        result = my_module.add_numbers(2, 3)
        self.assertEqual(result, 5)

    def test_multiply_numbers(self):
        result = my_module.multiply_numbers(4, 5)
        self.assertEqual(result, 20)


if __name__ == '__main__':
    unittest.main()
