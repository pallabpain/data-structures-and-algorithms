#!/usr/bin/env python
# pylint:disable=invalid-name

"""
This file contains the following implementations of binary search
1. Iterative binary search
2. Recursive binary search
3. Iterative binary search with reduced comparisons
"""

from __future__ import print_function


def binary_search(a, key):
    """
    Iterative binary search implmentation
    """
    lo, high = 0, len(a) - 1
    while lo <= high:
        mid = lo + (high - lo) // 2
        if a[mid] == key:
            return mid
        elif a[mid] > key:
            high = mid - 1
        elif a[mid] < key:
            lo = mid + 1
    return None


def binary_search_recursive(a, key, lo, high):
    """
    Recursive binary search implementation
    """
    if lo <= high:
        mid = lo + (high - lo) // 2
        if a[mid] == key:
            return mid
        if a[mid] > key:
            return binary_search_recursive(a, key, lo, mid - 1)
        return binary_search_recursive(a, key, mid + 1, high)
    return None


def binary_search_optimized(a, key):
    """
    Iterative binary search with reduced comparisons
    """
    lo, high = 0, len(a) - 1
    while high - lo > 1:
        mid = lo + (high - lo) // 2
        if a[mid] <= key:
            lo = mid
        else:
            high = mid
    return mid if a[mid] == key else None


if __name__ == "__main__":
    num_list = [1, 3, 4, 5, 6, 9, 11, 12, 15, 16, 17,
                19, 20, 21, 25, 100, 102, 1023, 1042, 1103, 1204]

    # Should match and return the index
    print(binary_search(num_list, 1023))
    # Shouldn't match and return None
    print(binary_search_recursive(num_list, 110, 0, len(num_list) - 1))
    # Should match and return the index
    print(binary_search(num_list, 11))
