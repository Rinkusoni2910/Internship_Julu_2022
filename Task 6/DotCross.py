import numpy
N=int(input())
A =(numpy.array([list(input().split()) for _ in range(N)], dtype=int))
B =(numpy.array([list(input().split()) for _ in range(N)], dtype=int))
print(numpy.dot(A,B))