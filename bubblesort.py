import numpy as np

def bubsort(nlist):
    for passnum in range(len(nlist)-1, 0, -1):
        for i in range(passnum):
            if nlist[i] > nlist[i + 1]:
                temp = nlist[i]
                nlist[i] = nlist[i + 1]
                nlist[i + 1] = temp

nlist = np.random.randint(low = 0, high = 20, size = 21)
bubsort(nlist)
print(nlist)
