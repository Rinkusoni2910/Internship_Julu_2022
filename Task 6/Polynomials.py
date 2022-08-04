import numpy
coeff_P=list(map(float,input().split()))
x=input()
print(numpy.polyval(coeff_P, int(x)))