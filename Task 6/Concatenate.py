import numpy
n, m, p = map(int, input().split())
array_n = numpy.array([input().strip().split() for _ in range(n)], int)
array_m = numpy.array([input().strip().split() for _ in range(m)], int)
print (numpy.concatenate((array_n, array_m), axis = 0))
