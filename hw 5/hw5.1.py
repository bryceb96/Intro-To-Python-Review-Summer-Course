import math
# File: hw5.1.py
# Author(s): Bryce Benjamin

# 1.a

str1 = 'This is a test of the emergency broadcast system.'

m1 = [4, 1, 5, 5, 1, 3, 8, 9, 7, 8, 2, 2, 6]

tup1 = ('curiouser', 'and', 'curiouser', 'cried', 'Alice')

set1 = {4, 7, 'a', True, 12.5, None}

d1 = {'hello': 5, 'goodbye': 3, 'you': 2, 'say': 8, 'I': 5, 'why': 4}
'''
print('\ntype(str1):', type(str1), '\nstr1:', str1)

print('\ntype(m1):', type(m1), '\nm1:', m1)

print('\ntype(tup1):', type(tup1), '\ntup1:', tup1)

print('\ntype(set1):', type(set1), '\nset1:', set1)

print('\ntype(d1):', type(d1), '\nd1:', d1)
'''

#1.b
m2 = [s for s in str1]
print("m2: ", m2)

#1.c 
tup2 = (t for t in tup1)
tup2 = ''.join(tup2)
tup2 = tuple(tup2)
print("tup2: ", tup2)

#1.d
set2 = set(str1)
print("set2: ", set2)
# the set is not ordered.

#1.e
m3 = list(tup1)
print("m3: ", m3)

#1.f
m4 = list(set1)
print("m4: ", m4)

#1.g
tup3 = tuple(m1)
print("tup3: ", tup3)

#1.h
tup4 = tuple(set1)
print("tup4: ", tup4)

#1.i
set3 = set(tup1)
print("set3: ", set3)
#set3 has only one curiouser, is ordered differently than tup1

#1.j
listk1 = list(d1.keys())
print("listk1: ", listk1)

#1.k
setk1 = set(d1.keys())
print("setk1: ", setk1)
# setk1 has the same number of listk1, however they are not ordered the same. If listk1 had repeating items then the amount of items compared to setk1 would be different

#1.l
print("length of d1 items: ", len(d1.items()))
print("Length of listk1 items: ", len(listk1))
print("Length of setk1: ", len(setk1))

#1.m
listv1 = list(d1.values())
print("listv1: ", listv1)

#1.n
setv1 = set(d1.values())
print("setv1: ", setv1)
#setv1 has one less item than listv1 since 5 is a duplicate number. Also setv1 happens to be ordered in ascendence, but that is by chance since sets are unordered and unindexed

#1.o
print("Length of d1 values: ", len(d1.values()))
print("Length of listv1: ", len(listv1))
print("Length of setv1: ", len(setv1))
#The keys of a dict must be hashable, meaning they cannot be changed, whereas a dictionary value is unhashable.
# however keys and values cannot be unique

#1.p
if m2[7] == tup2[7]:
    print("these m2[7] and tup2[7] values are equal")
else:
    print("these m2[7] and tup2[7] values are not equal")
    #they are not equal
    
#1.q
# only mq1, mq2, mq5, mq6, mq7 can be made as lists
    
#2.a
mc1 = [m - m for m in range(10)]
print("mc1: ", mc1)

#2.b
mc2 = [m for m in range(10)]
print("mc2: ", mc2)

#2.c
mc3 = [m ** 0.5 for m in range(10)]
print("mc3: ", mc3)

#2.d
mc4 = [m % 3 for m in range(15)]
print("mc4: ", mc4)
#2.e
n = 4
mc5 = [ (m, m + 1, (m + 2) ** 2) for m in range(10)]
print("mc5: ", mc5)

#3.a
str3a = str1
str3a.islower()
print("str3a: ", str3a)

#3.b
str3b = str3a
str3b = str3b.title()
print("str3b: ", str3b)

#3.c
m3c = str1.split(' ')
print("m3c: ", m3c)

#3.d 
m3d = m3c[:2] + m3c[5:7] + m3c[-1:]
print("m3d: ", m3d)

#3.e
str3e = m3d
str3e = ' '.join(str3e)
print("str3e: ", str3e)

#3.f
str3f = m3d
str3f = '+' + '+'.join(str3f) + '+'
print("str3f: ", str3f)

#3.g
str3g = str3f
str3g = str3g.upper()
print("str3g: ",str3g)

#3.f
ex_str = "Hello World"
print("ex_str centered: ", ex_str.center(25, '=') )
print("ex_str left justified: ", ex_str.ljust(25, '='))
print("ex_str right justified: ", ex_str.rjust(25, '='))
ex_str = "        Hello World       "
print("ex_str stripped: ", ex_str.strip())
print("ex_str left stripped: ", ex_str.lstrip())
print("ex_str right stripped: ", ex_str.rstrip())
print("ex_str is all lowercase?: ", ex_str.islower())
print("ex_str is all uppercase?: ", ex_str.isupper())
print("is ex_str alphabetic?: ", ex_str.isalpha())
print("is ex_str numeric?: ", ex_str.isnumeric())
print("is ex_str alphanumeric?: ", ex_str.isalnum())
