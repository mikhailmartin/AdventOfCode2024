import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from Day2_RedNosed_Reports import part1


@pytest.mark.parametrize(
    ("report", "expected"),
    [
        param([7, 6, 4, 2, 1], True),
        param([1, 2, 7, 8, 9], False),
        param([9, 7, 6, 2, 1], False),
        param([1, 3, 2, 4, 5], False),
        param([1, 3, 6, 7, 9], True),
    ],
)
def test_is_safe(report, expected):

    assert part1(report) == expected
