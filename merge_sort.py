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

    f, l = low, mid + 1
    t = [] # temporary list

    while f <= mid and l <= high:
        if array[f] < array[l]:
            t.append(array[f])
            f += 1
        else:
            t.append(array[l])
            l += 1

    if f <= mid:
        t.extend(array[f:mid + 1])

    if l <= high:
        t.extend(array[l:high + 1])

    i = 0
    # Update the original list with the sorted numbers
    while low <= high:
        array[low] = t[i]
        low += 1
        i += 1

a = [18, 3, 4, 5, 19, 20, -1, 0]
sort(a)
print a
