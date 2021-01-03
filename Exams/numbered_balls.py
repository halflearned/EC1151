import numpy as np

n_iter = 100000

balls = np.arange(1, 11)

no_rep = []
with_rep = []
for _ in range(n_iter):
    no_rep += [np.random.choice(balls, size = (4), replace = False)]
    with_rep += [np.random.choice(balls, size = (4), replace = False)]
