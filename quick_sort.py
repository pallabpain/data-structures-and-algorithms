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
    if low < high:
        pivot = partition(a, low, high)
        print 'pivot = ', pivot, ' array = ', a
        quick_sort(a, low, pivot - 1)
        quick_sort(a, pivot + 1, high)
