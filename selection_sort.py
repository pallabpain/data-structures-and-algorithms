#!/usr/bin/python env

'''
Selection sort implementation
'''

def selection_sort(a):
    ''' Selection sort algorithm '''
    n = len(a)
    for i in range(n):
        min_i = i
        for j in range(i + 1, n):
            if a[min_i] > a[j]:
                min_i = j
        a[i], a[min_i] = a[min_i], a[i]
