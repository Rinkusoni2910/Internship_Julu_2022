import math

def combination(n, x):
    return math.factorial(n) / (math.factorial(x) * math.factorial(n-x))

def binomial_distribution(x, n, p):
    return combination(n, x) * p**x * (1-p)**(n-x)

B, G = 1.09,1
z = B / G
print(round(sum([binomial_distribution(i, 6, z / (1 + z)) for i in range(3, 7)]), 3))