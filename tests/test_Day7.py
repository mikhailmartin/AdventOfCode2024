import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from Day7_Bridge_Repair import apply_operation, evaluate_expression


@pytest.mark.parametrize(
    ("operator", "a", "b", "expected"),
    [
        param("+", 1, 2, 3),
        param("*", 4, 5, 20),
        param("||", 45, 56, 4556)
    ],
)
def test_apply_operation(operator, a, b, expected):

    assert apply_operation(operator, a, b) == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        param("11+6+16+20", 53),
    ],
)
def test_evaluate_expression(expression, expected):

    assert evaluate_expression(expression) == expected
