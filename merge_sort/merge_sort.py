#!/usr/bin/env python

# Wrapper on top of mergesort function
def sort(array):
    mergesort(array, 0, len(array) - 1)


# In place merge sort function
def mergesort(array, low, high):
    mid = (low + high) / 2
    if low < high:
        mergesort(array, low, mid) # For left half
        mergesort(array, mid + 1, high) # For right half

    i, f, l = 0, low, mid + 1
    t = [None] * (high - low + 1) # Temporary list

    while f <= mid and l <= high:
        if array[f] < array[l]:
            t[i] = array[f]
            f += 1
        else:
            t[i] = array[l]
            l += 1
        i += 1

    if f <= mid:
        t[i:] = array[f:mid + 1]

    if l <= high:
        t[i:] = array[l:high + 1]

    i = 0
    # Update the original list with the sorted numbers
    while low <= high:
        array[low] = t[i]
        low += 1
        i += 1

