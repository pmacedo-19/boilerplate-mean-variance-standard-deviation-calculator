import numpy as np

def calculate(list):

    # Transforming list into a 3x3 numpy array
    arr = np.array(list).reshape(3, 3)
    
    # Sum line
    colsum = arr.sum(axis=0)
    linsum = arr.sum(axis=1)
    flatsum = arr.sum(axis=(0,1))

    # min line
    colmin = arr.min(axis=0)
    linmin = arr.min(axis=1)
    flatmin = arr.min(axis=(0,1))

    # max line
    colmax = arr.max(axis=0)
    linmax = arr.max(axis=1)
    flatmax = arr.max(axis=(0,1))

    # Std line
    colstd = arr.std(axis=0)
    linstd = arr.std(axis=1)
    flatstd = arr.std(axis=(0,1))

    # var line
    colvar = arr.var(axis=0)
    linvar = arr.var(axis=1)
    flatvar = arr.var(axis=(0,1))

    # mean line
    colmean = arr.mean(axis=0)
    linmean = arr.mean(axis=1)
    flatmean = arr.mean(axis=(0,1))



    print(arr)
    print(colvar)
    print(linvar)
    print(flatvar)

    return calculations