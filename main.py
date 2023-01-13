import numpy as np
import math


def calculate(lst):

    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")

    math.sqrt(len(lst)-9)
    matA = np.array([[lst[0], lst[1], lst[2]],
                     [lst[3], lst[4], lst[5]],
                     [lst[6], lst[7], lst[8]]])

    mean0 = matA.mean(axis=0)
    mean1 = matA.mean(axis=1)
    meanf = matA.mean()

    max0 = matA.max(axis=0)
    max1 = matA.max(axis=1)
    maxf = matA.max()

    min0 = matA.min(axis=0)
    min1 = matA.min(axis=1)
    minf = matA.min()

    sum0 = matA.sum(axis=0)
    sum1 = matA.sum(axis=1)
    sumf = matA.sum()

    desvest0 = np.std(matA, axis=0)
    desvest1 = np.std(matA, axis=1)
    desvestf = np.std(matA)

    var0 = matA.var(0)
    var1 = matA.var(1)
    varf = matA.var()

    diccionario = {
        'mean': [list(mean0), list(mean1), meanf],
        'variance': [list(var0), list(var1), varf],
        'standard deviation': [list(desvest0), list(desvest1), desvestf],
        'max': [list(max0), list(max1), maxf],
        'min': [list(min0), list(min1), minf],
        'sum': [list(sum0), list(sum1), sumf]
    }
    return diccionario


a = calculate([2,6,2,8,4,0,1])
print(a)