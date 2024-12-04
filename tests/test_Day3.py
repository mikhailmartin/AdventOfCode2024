import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from Day3_Mull_It_Over import main


PART1_PATTERN = r"mul\(\d{1,3},\d{1,3}\)"
PART2_PATTERN = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"


@pytest.mark.parametrize(
    ("pattern", "text", "expected"),
    [
        param(PART1_PATTERN, "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))", 161),
        param(PART2_PATTERN, "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))", 48)
    ],
)
def test_main(pattern, text, expected):

    assert main(pattern, text) == expected
