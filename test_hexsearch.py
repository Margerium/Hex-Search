import unittest

from hexsearch import formulate_grid
from hexsearch import grid
from hexsearch import convert_hex_string_to_hex_decimal
from hexsearch import cardinal_point_search
from hexsearch import strings_in_hex_to_search

test_list = [True, False, 0, -1, 0.314]


class IsInputGridValid(unittest.TestCase):

    def test_input_grid(self):
        result = formulate_grid(grid)
        self.assertEqual(result,
                         [['0x01', '0x00', '0xa8', '0x78', '0x48', '0xb7', '0x7f', '0xb8', '0x00', '0x86', '0x8a'],
                          ['0x2d', '0xe1', '0x07', '0x0c', '0x19', '0x86', '0x88', '0x00', '0x44', '0x47', '0x9a'],
                          ['0x34', '0x1e', '0x9d', '0xe7', '0x8f', '0x2d', '0x99', '0x66', '0x00', '0x2a', '0x1a'],
                          ['0x43', '0x68', '0x72', '0x69', '0x73', '0x74', '0x6d', '0x61', '0x73', '0x0a', '0x75'],
                          ['0xd0', '0x6d', '0x8e', '0x54', '0x74', '0xde', '0x2e', '0x34', '0x00', '0xf8', '0xdd'],
                          ['0x55', '0xa0', '0xa3', '0x6e', '0x6e', '0x3f', '0x95', '0xbb', '0x74', '0xa1', '0x5a'],
                          ['0x80', '0x00', '0x61', '0x00', '0x65', '0x69', '0xc0', '0xa8', '0x00', '0x01', '0xef'],
                          ['0x3f', '0x69', '0x4d', '0x9c', '0x73', '0x20', '0xb9', '0xff', '0x6c', '0xc9', '0x45'],
                          ['0x40', '0xa2', '0x42', '0x58', '0x65', '0x27', '0xa6', '0xaa', '0x13', '0x2b', '0x32'],
                          ['0x5a', '0x79', '0xef', '0x50', '0x72', '0x84', '0x73', '0x60', '0xe9', '0xc5', '0x29'],
                          ['0xaf', '0x4c', '0x00', '0xe0', '0x50', '0x8d', '0x78', '0xc2', '0x0f', '0x0b', '0xe8']])

        result = formulate_grid("")
        self.assertEqual(result, "formulate grid is expecting an input in the form of a list! "
                                 "Please check the file containing the grid!")

        result = formulate_grid(True)
        self.assertEqual(result, "formulate grid is expecting an input in the form of a list! "
                                 "Please check the file containing the grid!")

        result = formulate_grid(False)
        self.assertEqual(result, "formulate grid is expecting an input in the form of a list! "
                                 "Please check the file containing the grid!")

        result = formulate_grid(0)
        self.assertEqual(result, "formulate grid is expecting an input in the form of a list! "
                                 "Please check the file containing the grid!")

        result = formulate_grid(-1)
        self.assertEqual(result, "formulate grid is expecting an input in the form of a list! "
                                 "Please check the file containing the grid!")

        result = formulate_grid(0.314)
        self.assertEqual(result, "formulate grid is expecting an input in the form of a list! "
                                 "Please check the file containing the grid!")

        result = formulate_grid(314000000000000)
        self.assertEqual(result, "formulate grid is expecting an input in the form of a list! "
                                 "Please check the file containing the grid!")


class IsHexStringOutputCorrect(unittest.TestCase):

    def test_output_strings(self):
        result = convert_hex_string_to_hex_decimal()
        self.assertEqual(result, [['0x43', '0x68', '0x72', '0x69', '0x73', '0x74', '0x6d', '0x61', '0x73', '0x0a'],
                                  ['0x50', '0x72', '0x65', '0x73', '0x65', '0x6e', '0x74', '0x73'],
                                  ['0x40', '0x69', '0x61', '0x6e', '0x74'],
                                  ['0x00', '0x44', '0x00', '0x73', '0x00', '0x74', '0x00', '0x6c'],
                                  ['0x19', '0x0c', '0x07', '0xe1'], ['0x5a', '0x40', '0x3f', '0x80'],
                                  ['0x7f', '0x00', '0x00', '0x0a'], ['0xc0', '0xa8', '0x00', '0x01'],
                                  ['0x07', '0x9d', '0x72', '0x8e', '0xa3', '0x61']]
                         )


class IsStringsToSearchValid(unittest.TestCase):

    def test_strings_to_search(self):
        result = cardinal_point_search(strings_in_hex_to_search)
        self.assertEqual(result, "The operation completed successfully")

        result = cardinal_point_search("")
        self.assertEqual(result, "expecting a list of strings to search, check your strings_to_search variable!")

        result = cardinal_point_search(True)
        self.assertEqual(result, "expecting a list of strings to search, check your strings_to_search variable!")

        result = cardinal_point_search(False)
        self.assertEqual(result, "expecting a list of strings to search, check your strings_to_search variable!")

        result = cardinal_point_search(0)
        self.assertEqual(result, "expecting a list of strings to search, check your strings_to_search variable!")

        result = cardinal_point_search(-1)
        self.assertEqual(result, "expecting a list of strings to search, check your strings_to_search variable!")

        result = cardinal_point_search(0.314)
        self.assertEqual(result, "expecting a list of strings to search, check your strings_to_search variable!")

        result = cardinal_point_search(314000000000000)
        self.assertEqual(result, "expecting a list of strings to search, check your strings_to_search variable!")

        result = cardinal_point_search(test_list)
        self.assertEqual(result, "expecting list to contain string entries, check your strings_to_search variable!")