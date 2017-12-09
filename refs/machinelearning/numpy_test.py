import numpy as np

print np.version.full_version

# numpy array
a = np.array([0, 1, 2, 3, 4, 5])
print a
print a.ndim
print a.shape

# numpy matrix
b = a.reshape((3, 2))
print b
print b.ndim
print b.shape

# non-copy
b[1][0] = 77
print b
print a

# copy
c = a.reshape((3, 2)).copy()
print c
c[0][0] = -99
print a
print c

# array operation apply to each element
print a*2
print a**2

# array as index
print a[np.array([2, 3, 4])]

# bool condition apply to each element
print a>4
print a[a>4]
# correct abnormal data
a[a>4] = 4
print a
# special func to do above work
a1 = a.clip(0, 3)
print a1

# numpy.NAN
c = np.array([1, 2, np.NAN, 3, 4])
print c
print np.isnan(c)
print c[~np.isnan(c)]
print np.mean(c[~np.isnan(c)])

# numpy data type
a = np.array([1, 2, 3])
print a.dtype
s = np.array(['1', 'stringy'], dtype='|S8')
print s.dtype
o =  np.array([1, 'stringy', set([1, 2, 3])])
print o.dtype
