#!/usr/bin/env python

'''
Insertion sort implementation
'''

def insertion_sort(a):
    ''' Insertion sort algorithm '''
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
