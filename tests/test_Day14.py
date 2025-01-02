import os
import sys

import numpy as np

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from Day14_Restroom_Redoubt import (
    get_position_after_n_steps, get_matrix_after_n_steps, count_robots_in_quadrants
)


@pytest.mark.parametrize(
    ("px", "py", "vx", "vy", "n_steps", "map_size_x", "map_size_y", "expected"),
    [
        param(2, 4, 2, -3, 1, 11, 7, (4, 1)),
        param(2, 4, 2, -3, 2, 11, 7, (6, 5)),
        param(2, 4, 2, -3, 3, 11, 7, (8, 2)),
        param(2, 4, 2, -3, 4, 11, 7, (10, 6)),
        param(2, 4, 2, -3, 5, 11, 7, (1, 3)),
    ],
)
def test_get_position_after_n_steps(
    px, py, vx, vy, n_steps, map_size_x, map_size_y, expected
):

    assert get_position_after_n_steps(
        px, py, vx, vy, n_steps, map_size_x, map_size_y
    ) == expected


def test_get_matrix_after_n_steps():

    robots = [
        (0, 4, 3, -3),
        (6, 3, -1, -3),
        (10, 3, -1, 2),
        (2, 0, 2, -1),
        (0, 0, 1, 3),
        (3, 0, -2, -2),
        (7, 6, -1, -3),
        (3, 0, -1, -2),
        (9, 3, 2, 3),
        (7, 3, -1, 2),
        (2, 4, 2, -3),
        (9, 5, -3, -3),
    ]

    matrix = np.zeros((11, 7), dtype=np.int64)
    matrix[0, 2] = 1
    matrix[1, 3] = 1
    matrix[1, 6] = 1
    matrix[2, 3] = 1
    matrix[3, 5] = 1
    matrix[4, 5] = 2
    matrix[5, 4] = 1
    matrix[6, 0] = 2
    matrix[6, 6] = 1
    matrix[9, 0] = 1

    result = get_matrix_after_n_steps(robots, 100, 11, 7)

    assert np.all(result == matrix)


def test_count_robots_in_quadrants():

    matrix = np.zeros((11, 7), dtype=np.int64)
    matrix[0, 2] = 1
    matrix[1, 3] = 1
    matrix[1, 6] = 1
    matrix[2, 3] = 1
    matrix[3, 5] = 1
    matrix[4, 5] = 2
    matrix[5, 4] = 1
    matrix[6, 0] = 2
    matrix[6, 6] = 1
    matrix[9, 0] = 1

    q1, q2, q3, q4 = count_robots_in_quadrants(matrix)

    assert (q1, q2, q3, q4) == (1, 3, 4, 1)
