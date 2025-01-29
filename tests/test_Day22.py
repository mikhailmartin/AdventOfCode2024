import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from Day22_Monkey_Market import mix, prune, tick


def test_mix():
    assert mix(15, 42) == 37


def test_prune():
    assert prune(100000000) == 16113920


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        param(1, 8685429),
    ],
)
def test_tick(number, expected):

    assert tick(number, 2000) == expected
