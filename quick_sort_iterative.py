#!/usr/bin/env python

def partition(a, low, high):
    '''
    Creates left and right partitions and returns
    index of the pivot
    '''
    i = low - 1
    pivot = a[high]
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1

def quick_sort(a, low, high):
    ''' Function for sorting numbers using quick sort algorithm'''
    stack = [low, high]
    while stack:
        high = stack.pop()
        low = stack.pop()

        pivot = partition(a, low, high)

        if pivot - 1 > low:
            stack.append(low)
            stack.append(pivot - 1)

        if pivot + 1 < high:
            stack.append(pivot + 1)
            stack.append(high)
