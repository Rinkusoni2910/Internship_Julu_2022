import numpy 
N,M=map(int,input().strip().split(' '))
arr =(numpy.array([list(input().split()) for _ in range(N)], dtype=int))
print(numpy.prod(numpy.sum(arr, axis=0)))