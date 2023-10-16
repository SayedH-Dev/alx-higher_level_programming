#!usr/bin/python3
""" defines unittest for Square """
import unittest
import io
import unittest.mock
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_init(self):
        s1 = Square(5)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        s2 = Square(3, 2, 1, 100)
        self.assertEqual(s2.id, 100)
        self.assertEqual(s2.size, 3)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 1)

    def test_area(self):
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

        s2 = Square(3, 2, 1, 100)
        self.assertEqual(s2.area(), 9)

    def test_display(self):
        s1 = Square(3)
        expected_output = "###\n###\n###\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            s1.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

        s2 = Square(2, 1, 1)
        expected_output = "\n ##\n ##\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            s2.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        s1 = Square(5, 2, 1, 1)
        self.assertEqual(str(s1), "[Square] (1) 2/1 - 5")

        s2 = Square(3, 0, 0, 100)
        self.assertEqual(str(s2), "[Square] (100) 0/0 - 3")

    def test_update(self):
        s1 = Square(5, 2, 1, 1)
        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 2/1 - 5")

        s2 = Square(3, 0, 0, 100)
        s2.update(10, 3, 2, 1)
        self.assertEqual(str(s2), "[Square] (10) 2/1 - 3")

    def test_to_dictionary(self):
        s1 = Square(5, 2, 1, 1)
        s1_dict = s1.to_dictionary()
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 1}
        self.assertEqual(s1_dict, expected_dict)

        s2 = Square(3, 0, 0, 100)
        s2_dict = s2.to_dictionary()
        expected_dict = {'id': 100, 'size': 3, 'x': 0, 'y': 0}
        self.assertEqual(s2_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()
