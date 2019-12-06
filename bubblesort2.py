#! /usr/bin/python

import numpy as np

def sort(arr):
    while True:
        corrected = False
        for i in range(0, len(arr) -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                corrected = True
        if not corrected:
            return arr


print(sort(np.random.normal(size = 1000)))
# best-case scenario O(n)
# print(sort([1, 2, 3, 4, 5, 6]))
# average scenario O(n^2)
# print(sort([4, 2, 3, 1, 6, 5]))
# worset-case scenario O(n^2)
# print(sort([6, 5, 4, 3, 2, 1]))
