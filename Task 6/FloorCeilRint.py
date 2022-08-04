import numpy
numpy.set_printoptions(legacy='1.13')
arr = input().strip().split(' ')
A=numpy.array(arr,float)
print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))