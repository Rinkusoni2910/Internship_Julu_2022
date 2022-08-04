import numpy
N,M=map(int,input().strip().split(' '))
arr =(numpy.array([list(input().split()) for _ in range(N)], dtype=int))
print(numpy.mean(arr, axis=1))
print(numpy.var(arr, axis=0))
print(round(numpy.std(arr, axis = None),11))