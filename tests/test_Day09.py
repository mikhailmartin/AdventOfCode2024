import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from Day09_Disk_Fragmenter import part2


@pytest.mark.parametrize(
    ("disk_map", "expected"),
    [
        param("2333133121414131402", 2858),
        param("1313165", 169)
    ],
)
def test_part2(disk_map, expected):

    assert part2(disk_map) == expected
