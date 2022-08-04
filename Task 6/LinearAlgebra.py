import numpy
N=int(input())
arr =(numpy.array([list(input().split()) for _ in range(N)], dtype=float))
print(round(numpy.linalg.det(arr),2))