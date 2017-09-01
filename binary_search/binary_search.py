#!/usr/bin/env python

# Iterative binary search implmentation
def binary_search(a, key):
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


# Recursive binary search implementation
def binary_search_recursive(a, key, lo, high):
    if lo <= high:
        mid = lo + (high - lo) // 2
        if a[mid] == key:
            return mid
        elif a[mid] > key:
            return binary_search_recursive(a, key, lo, mid - 1)
        else:
            return binary_search_recursive(a, key, mid + 1, high)
    else:
        return None


# Iterative binary search with reduced comparisons
def binary_search_optimized(a, key):
    lo, high = 0, len(a) - 1
    while high - lo > 1:
        mid = lo + (high - lo) / 2
        if a[mid] <= key:
            lo = mid
        else:
            high = mid
    return mid if a[mid] == key else None

    

num_list = [1, 3, 4, 5, 6, 9, 11, 12, 15, 16, 17, 19, 20, 21, 25, 100, 102, 1023, 1042, 1103, 1204]

print(binary_search(num_list, 1023))

print(binary_search_recursive(num_list, 110, 0, len(num_list) - 1))

print(binary_search(num_list, 11))