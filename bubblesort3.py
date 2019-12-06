import numpy as np
import matplotlib.pyplot as plt
import random

def bubsort(arr):
    while True:
        corrected = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                corrected = True
                plt.plot(arr)
                plt.draw()
                plt.pause(0.000000000000001)
                plt.clf()
        if not corrected:
            return arr
            plt.plot(arr)

arr = np.random.randint(low = 0, high = 20, size = 21)
bubsort(arr)
