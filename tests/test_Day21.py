import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from Day21_Keypad_Conundrum import Solution


NUMERIC_KEYPAD = [
    "789",
    "456",
    "123",
    "#0A",
]


@pytest.mark.parametrize(
    ("keypad", "src_dst", "expected"),
    [
        param(NUMERIC_KEYPAD, ("A", "0"), ["<A"]),
        param(NUMERIC_KEYPAD, ("0", "2"), ["^A"]),
        param(NUMERIC_KEYPAD, ("2", "9"), ["^^>A", ">^^A"]),
        param(NUMERIC_KEYPAD, ("9", "A"), ["vvvA"]),
    ],
)
def test_get_moves(keypad, src_dst, expected):

    solution = Solution()
    assert solution.get_paths(keypad)[src_dst] == expected
