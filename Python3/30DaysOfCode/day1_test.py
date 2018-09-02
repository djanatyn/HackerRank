#!/usr/bin/env python3

from unittest.mock import patch
import unittest
import io
import sys

test_case = [
    '12',
    '4.0',
    'is the best place to learn and practice coding!'
]

expected_output = [
    '16.0',
    '8.0',
    'HackerRank is the best place to learn and practice coding!'
]


class DayOne(unittest.TestCase):

    output = io.StringIO()
    sys.stdout = output

    @patch('builtins.input', side_effect=test_case)
    def test(self, mock):
        import day1

if __name__ == '__main__':
    unittest.main()
