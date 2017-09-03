#!/usr/bin/env python

def bubble_sort(a):
    ''' Function to sort a list using bubble sort '''
    n = len(a)
    for i in xrange(n):
        swapped = False
        for j in xrange(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break

array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
bubble_sort(array)
print array
