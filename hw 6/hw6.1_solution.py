
# hw6.1_solution.py
# Authors:

# 1.a.
import numpy as np

a1 = np.arange(6,11)
print(a1)

# 1.b.
aobs = np.genfromtxt('observations.csv', delimiter=',')
print('aobs:')
print(aobs)
print('aobs.shape:', aobs.shape)
print('aobs.ndim:', aobs.ndim)

# 1.c.
print('aobs[:8]:')    # or aobs[0:8]
print(aobs[:8])

# 1.d.
print('aobs[-4:]:')   # or aobs[16:] or aobs[16:20]
print(aobs[-4:])

# 1.e.
num_p = len(aobs)
first_i = (num_p - 10) // 2
last_i = first_i + 10
print('aobs middle 10:')
print(aobs[first_i:last_i])

# 1.f.
print('aobs[:, 0]:')
print(aobs[:, 0])

# 1.g.
print('aobs[:, 1:]:')
print(aobs[:, 1:])

# 1.h.
print('aobs middle 10 heights, weights:')
print(aobs[first_i:last_i, 1:])

# 1.i.
print('aobs first 10 ages and weights:')
print(aobs[:10, [True, False, True]])

# 1.j.
print('Boolean index for rows where height >= 70:')
print(aobs[:, 1] >= 70)

# 1.k.
print('Rows where height >= 70:')
print(aobs[aobs[:, 1] >= 70])

# 1.l.
a2 = np.array([1, 2, 3, 4, 6])
print('a2.mean():', a2.mean())
print('a2.min():', a2.min())
print('a2.max():', a2.max())
print('a2.std():', a2.std())

# 1.m.
# a data set is perfectly correlated with itself
print('np.corrcoef(a1, a1):')
print(np.corrcoef(a1, a1))
# a1 and a2 are highly but not perfectly correlated
print('np.corrcoef(a1, a2):')
print(np.corrcoef(a1, a2))

# 1.n
# ages are column sub-0
print('Patient ages:')
print('mean: ', aobs[:, 0].mean())
print('min:  ', aobs[:, 0].min())
print('max:  ', aobs[:, 0].max())
print('std:  ', aobs[:, 0].std())

# 1.o
# heights are column sub-1
print('Patient heights:')
print('mean: ', aobs[:, 1].mean())
print('min:  ', aobs[:, 1].min())
print('max:  ', aobs[:, 1].max())
print('std:  ', aobs[:, 1].std())

# 1.p
# weights are column sub-2
print('Patient weights:')
print('mean: ', aobs[:, 2].mean())
print('min:  ', aobs[:, 2].min())
print('max:  ', aobs[:, 2].max())
print('std:  ', aobs[:, 2].std())

# 1.q
# age/height correlation
print('age/height correlation:')
print(np.corrcoef(aobs[:, 0], aobs[:, 1]))
# correlation is not significant, since all of the patients are adults:
# we would see a greater correlation if we had children of several ages

# 1.r
# age/weight correlation
print('age/weight correlation:')
print(np.corrcoef(aobs[:, 0], aobs[:, 2]))
# again, correlation is not significant, since all of the patients are adults:
# we would see a greater correlation if we had childern of several ages

# 1.s
# age/height correlation
print('height/weight correlation:')
print(np.corrcoef(aobs[:, 1], aobs[:, 2]))
# as we would expect, there is a positive correlation between height and weight


