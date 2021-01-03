import numpy as np

n_students = 20
n_stars = 20
n_iter = 100000

p = [1/n_students]*n_students
stars = np.random.multinomial(n_stars, p, size = n_iter)

m = np.mean(np.sum(stars == 0, 1))
print(m)
print(20*(19/20)**20)
