import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from Day22_Monkey_Market import mix, prune, tick, get_prices, get_changes


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

    for _ in range(2000):
        number = tick(number)

    assert number == expected


def test_get_prices():
    assert get_prices(123, 9) == [3, 0, 6, 5, 4, 4, 6, 4, 4, 2]


def test_get_changes():
    assert get_changes([3, 0, 6, 5, 4, 4, 6, 4, 4, 2]) == [-3, 6, -1, -1, 0, 2, -2, 0, -2]
