# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 22:24:06 2020

@author: Bryce
"""
import numpy as np

#6.1a
a1 = np.array([6,7,8,9,10])
print(a1)

#6.1b
aobs = np.genfromtxt('observations.csv', delimiter = ',' )
print(aobs)
print(aobs.shape)
print(aobs.ndim)

#6.1c 
print("First eight patient records: \n", aobs[0:8])
print("\n")
#6.1d
print("Last 4 patient records: \n", aobs[16:])
print("\n")
#6.e
print("Middle 10 patient records: \n", aobs[5:15])
print("\n")
#6.f
print("Ages of all the patients: \n", aobs[:, [0]])
#6.g
print("\n")
print("Heights and Weights of all patients: \n", aobs[:, [1,2]])
#6.h
print("\n")
print("Heights and weights of the middle 10 patients: \n", aobs[5:15, [1,2]])
#6.i
print("\n")
print("Ages and Weights of the first 10 patients: \n", aobs[:,[True,False,True]])
#6.j
print("\n")
print(aobs[:, [0, 1, 2]] > 70)
#6.k
print("\n")
print(aobs[aobs[:, 1] >= 70])

#6.l
print("\n")
a2 = np.array([1, 2, 3, 4, 6])
print("a2: ", a2)
print("a2 means: ", a2.mean())
print("a2 min: ", a2.min())
print("a2 max: ", a2.max())
print("a2 standard deviation: ", a2.std())
#6.1m
print("\n")
print(np.corrcoef(a1, a2))
#6.1n
print("\n")
aobs_ages = aobs[:, 0]
aobs_heights = aobs[:, 1]
aobs_weights = aobs[:, 2]
print("mean age of aobs: ", aobs_ages.mean())
print("min age of aobs: ", aobs_ages.min())
print("max age of aobs: ", aobs_ages.max())
print("standard deviation of aobsn ages: ", aobs_ages.std())
#6.1o
print("\n")
print("mean age of aobs: ", aobs_heights.mean())
print("min age of aobs: ", aobs_heights.min())
print("max age of aobs: ", aobs_heights.max())
print("standard deviation of aobs heights: ", aobs_heights.std())
#6.1 p
print("\n")
print("mean age of aobs: ", aobs_weights.mean())
print("min age of aobs: ", aobs_weights.min())
print("max age of aobs: ", aobs_weights.max())
print("standard deviation of aob weights: ", aobs_weights.std())
#6.1 q
print("\n")
print("correlation between ages and heights of aobs: ", np.corrcoef(aobs_ages, aobs_heights))
#this is not what I expected, as I do not understand what the nan output means.
#6.1 r
print("\n")
print("correlation between ages and weights of aobs: ", np.corrcoef(aobs_ages, aobs_weights))
#not what I expected, unsure what nan output means
#6.1 s
print("\n")
print("correlation between heights and weights of aobs: ", np.corrcoef(aobs_heights, aobs_weights))
#not what I expected, unsure what nan output means
