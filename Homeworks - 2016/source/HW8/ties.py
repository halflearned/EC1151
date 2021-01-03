import numpy as np
import itertools as it
from scipy.special import factorial

def break_ties(original):
    
    """"
    Example usage

    break_ties([0,1,0,2,1])

    should output

    array([[ 0.,  2.,  1.,  4.,  3.],
           [ 1.,  3.,  0.,  4.,  2.],
           [ 0.,  2.,  1.,  4.,  3.],
           [ 1.,  3.,  0.,  4.,  2.]])

    """"

    ranks, counts = np.unique(original, return_counts = True)
    cumcounts = np.cumsum(counts)
    
    n = int(np.prod([factorial(c) for c in counts])) # 2!*2!*1!
    out = np.zeros((n, len(original))) # Initialize

    for k, rank in enumerate(ranks):
        pos = np.argwhere(original == rank).flatten()  
        cycle_perms = it.cycle(it.permutations(pos))
        for row in range(n): 
            r = cumcounts[k - 1] if k > 0 else 0
            for p in next(cycle_perms):
                out[row, p] = r
                r += 1
    
    return out
    
