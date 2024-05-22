from islands_calculator import get_islands_count_recursive
import numpy as np
import pytest


@pytest.mark.parametrize("shape,matrix,output", [
    ((3, 3), np.array([
        [0, 1, 0],
        [0, 0, 0],
        [0, 1, 1],
    ]), 2),
    ((3, 4), np.array([
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
    ]), 3),
    ((3, 4), np.array([
        [0, 0, 0, 1],
        [0, 0, 1, 1],
        [0, 1, 0, 1],
    ]), 2),
])
def test_get_islands_count_2d(shape, matrix, output):
    assert get_islands_count_recursive(shape, matrix) == output
