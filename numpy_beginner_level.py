import numpy as np

a = np.array([[1,2,3,4,5,6],[2,3,5,7,5,7]])
print('Original array ', a.shape, ':')
print(a)

print("\nDimension: ", a.ndim, "\nSize: ", a.shape)

# Get a specific element (i.g. a[2,3]) 
print('a[2,3] = ', a[1,2])

# Get a specific row and colomn
print('First row: ', a[0,:], '\nThird colomn: ', a[:,2])

# Get specific elements [startIndex:endIndex:stepSize]
print('Get specific elements: ', a[1,1:6:1])

# Change a specific element in original array, or even
# series of number
print('\nIf a[2,4] = 20, then array: ')
a[1,3] = 20
print(a)
print('Whole 6th colomn equals to 15')
a[:,5] = 15
print(a)

print('\nArray a(3,5)of zeros: ')
print(np.zeros((3,5)))
print('Array a(5,2) of ones: ')
print(np.ones((5,2)))
print('Array a(4,4) of 44')
print(np.full((4,4),44))
print('\nRandom decimal numbers (4,3): ')
print(np.random.rand(4,3) * 10, '\n\nRandom decimal numbers (2,3,4): ')
print(np.random.rand(2,3,4) * 10)
print('\nRandom integer numbers (3,4) from 0 to 10: ')
print(np.random.randint(10,size=(3,4)))

# To copy array
a = np.array([1,2,3])
print('\nOriginal array a: ', a)
b = a.copy()
b[0] = 100
print('Array b (using b = a.copy): ', b)
print('Array a: ', a)
c = a
c[0] = 40
print('Array c (using c = a): ', c)
print('Array a: ', a)

# Mathematics
print('\nDo some math')
d = np.array([1,2,3,4])
print('Original array d = ', d)
print('d + 3 = ', d + 3)
print('d - 2 = ', d - 2)
print('d * 2 = ', d * 2)
print('d / 2 = ', d / 2)
e = np.array([1,10,3,1])
print('e = ', e, '\nd + e = ', d + e)

# Linear algebra
print('\nLenear algebra')
f = np.ones((4,4))
print('Array f: ')
print(f)
g = np.full((4,2),2)
print('Array g: ')
print(g)
print('Matrix multiplication (h = f*g): ')
h = np.matmul(f,g)
print(h)
i = np.identity(3)
print('Determinant:: ', np.linalg.det(i))

# Statistics
print('\nStatistics')
stats = np.array([[34,23,56],[76,32,29],[24,55,75]])
print('Original array')
print(stats)
print('min = ', np.min(stats), '\nmax = ',np.max(stats))

# Reorganizing arrays
before = np.array([[11,10,2,4],[6,5,8,10],[3,2,4,5]])
print('\nReorganizing arrays\nBefore', before.shape, ':')
print(before, '\nReshape (4,3)')
print(before.reshape((4,3)))

# Miscellaneous
print('\nRead from the file: ')
m = np.genfromtxt('data.txt', delimiter=',')
print(m)
