import copy
import pytest
from utils import sorting


@pytest.mark.test_insertion_sort
def test_insertion_sort():
    arr = []
    assert sorting.insertion_sort(arr) == []

    arr = [1]
    assert sorting.insertion_sort(arr) == [1]

    arr = [1, 2, 3]
    assert sorting.insertion_sort(arr) == [1, 2, 3]

    arr = [6, 5, 3, 1, 8, 7, 4, 2]
    sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8]
    assert sorting.insertion_sort(arr) == sorted_arr


@pytest.mark.test_quick_sort
def test_quick_sort():
    arr = [6, 5, 3, 1, 8, 7, 4, 2]

    arr_copy = copy.copy(arr)
    pivot_idx = sorting.partition(arr_copy, begin=0, end=len(arr_copy) - 1)
    assert pivot_idx == 5
    assert arr_copy == [2, 5, 3, 1, 4, 6, 8, 7]

    sorting.quick_sort(arr)
    assert arr == [1, 2, 3, 4, 5, 6, 7, 8]
