# -*- coding: utf-8 -*-
import copy


def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]
    
    n = len(arr)
    swapped = True

    x = 0
    while swapped:
        swapped = False
        for i in range(1, n-x):
            if arr[i-1] > arr[i]:
                swap(i-1, i)
                swapped = True
    
    return arr


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i  # the index of minimum value

        for j in range(i+1, len(arr)):  # select the smallest value
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[min_idx], arr[i] = arr[i], arr[min_idx]

    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):  # if given empty list, `len(arr)` equals 0, nothing is done
        cursor = arr[i]
        pos = i

        while pos > 0 and arr[pos - 1] > cursor:
            arr[pos] = arr[pos - 1]  # move elements to right
            pos -= 1
        arr[pos] = cursor

    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    # merge
    return merge(left, right, arr.copy())


def merge(left, right, merged):
    i, j = 0, 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged[k] = left[i]
            i += 1
        else:
            merged[k] = right[j]
            j += 1
        k += 1

    for n in range(i, len(left)):
        merged[k] = left[n]
        k += 1
    for n in range(j, len(right)):
        merged[k] = right[n]
        k += 1

    return merged


def partition(array, begin, end):
    pivot_idx = begin
    for i in range(begin + 1, end + 1):
        if array[i] <= array[begin]:
            pivot_idx += 1
            array[i], array[pivot_idx] = array[pivot_idx], array[i]
    array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
    return pivot_idx


def quick_sort_recursion(array, begin, end):
    if begin >= end:
        return
    pivot_idx = partition(array, begin, end)
    quick_sort_recursion(array, begin, pivot_idx - 1)
    quick_sort_recursion(array, pivot_idx + 1, end)


def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1

    return quick_sort_recursion(array, begin, end)


def check_sorting(sorting, arr):
    print('sorting with {}'.format(sorting.__name__))
    print('before:{}'.format(arr))
    print('after:{}\n'.format(sorting(copy.copy(arr))))


if __name__ == "__main__":
    arr = [6, 5, 3, 1, 8, 7, 4, 2]

    check_sorting(bubble_sort, arr)
    check_sorting(selection_sort, arr)
    check_sorting(insertion_sort, arr)
    check_sorting(merge_sort, arr)
