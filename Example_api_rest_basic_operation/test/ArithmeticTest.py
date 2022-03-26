import unittest

from operation.Arithmetic import Operation
from operation.ArithmeticError import Error


class ArithmeticTest(unittest.TestCase):

    def test_class_instantiation_incorrect_data_type(self):
        v1 = ["A"]
        v2 = [3]
        with self.assertRaisesRegex(Error, "Invalid data type"):
            Operation(v1, v2)

    def test_class_instantiation_incorrect_list_length(self):
        v1 = [3, 4]
        v2 = [3]
        with self.assertRaisesRegex(Error, "Lists of values should have same length"):
            Operation(v1, v2)

    def test_sum(self):
        v1 = [3]
        v2 = [3]
        self.assertEqual([6], Operation(v1, v2).sum())

    def test_subtract(self):
        v1 = [3]
        v2 = [3]
        self.assertEqual([0], Operation(v1, v2).subtract())

    def test_multiply(self):
        v1 = [3]
        v2 = [3]
        self.assertEqual([9], Operation(v1, v2).multiply())

    def test_divide(self):
        v1 = [3]
        v2 = [3]
        self.assertEqual([1], Operation(v1, v2).divide())

    def test_divide_by_zero(self):
        v1 = [3]
        v2 = [0]
        with self.assertRaisesRegex(Error, "Invalid division by zero"):
            Operation(v1, v2).divide()


if __name__ == '__main__':
    unittest.main()
