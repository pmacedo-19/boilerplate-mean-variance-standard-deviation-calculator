import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
        
    else:
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


        calculations = {}

        # Sending mean calculations to the dict
        calculations.setdefault('mean', []).append(colmean.tolist())
        calculations['mean'].append(linmean.tolist())
        calculations['mean'].append(flatmean)

        # Sending var calculations to the dict
        calculations.setdefault('variance', []).append(colvar.tolist())
        calculations['variance'].append(linvar.tolist())
        calculations['variance'].append(flatvar)

        # Sending std calculations to the dict
        calculations.setdefault('standard deviation', []).append(colstd.tolist())
        calculations['standard deviation'].append(linstd.tolist())
        calculations['standard deviation'].append(flatstd)

        # Sending max calculations to the dict
        calculations.setdefault('max', []).append(colmax.tolist())
        calculations['max'].append(linmax.tolist())
        calculations['max'].append(flatmax)

        # Sending min calculations to the dict
        calculations.setdefault('min', []).append(colmin.tolist())
        calculations['min'].append(linmin.tolist())
        calculations['min'].append(flatmin)

        # Sending sum calculations to the dict
        calculations.setdefault('sum', []).append(colsum.tolist())
        calculations['sum'].append(linsum.tolist())
        calculations['sum'].append(flatsum)

        return calculations