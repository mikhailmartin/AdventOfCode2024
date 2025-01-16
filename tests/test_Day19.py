import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from Day19_Linen_Layout import count_possible


@pytest.mark.parametrize(
    ("design", "available_towels", "expected"),
    [
        param("brwrr", ("r", "wr", "b", "g", "bwu", "rb", "gb", "br"), 2),
        param("bggr", ("r", "wr", "b", "g", "bwu", "rb", "gb", "br"), 1),
        param("gbbr", ("r", "wr", "b", "g", "bwu", "rb", "gb", "br"), 4),
        param("rrbgbr", ("r", "wr", "b", "g", "bwu", "rb", "gb", "br"), 6),
        param("bwurrg", ("r", "wr", "b", "g", "bwu", "rb", "gb", "br"), 1),
        param("brgr", ("r", "wr", "b", "g", "bwu", "rb", "gb", "br"), 2),
        param("ubwu", ("r", "wr", "b", "g", "bwu", "rb", "gb", "br"), 0),
        param("bbrgwb", ("r", "wr", "b", "g", "bwu", "rb", "gb", "br"), 0),
    ],
)
def test_foo(design, available_towels, expected):

    assert count_possible(design, available_towels) == expected
