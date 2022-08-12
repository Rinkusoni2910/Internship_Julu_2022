import math

def combination(n, x):
    return math.factorial(n) / (math.factorial(x) * math.factorial(n-x))

def binomial_distribution(x, n, p):
    return combination(n, x) * p**x * (1-p)**(n-x)

percentage, size = list(map(int, input().split(" ")))
print(round(sum([binomial_distribution(i,size,percentage/100) for i in range(3)]), 3))
print(round(sum([binomial_distribution(i,size,percentage/100) for i in range(2, size+1)]), 3))
