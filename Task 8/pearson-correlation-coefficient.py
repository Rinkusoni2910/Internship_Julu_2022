n= int(input())
x = list(map(float,input().strip().split()))
y = list(map(float,input().strip().split()))
meanx = sum(x) / n
meany = sum(y) / n
std_dev_x = (sum([(i - meanx)**2 for i in x]) / n)**0.5
std_dev_y = (sum([(i - meany)**2 for i in y]) / n)**0.5
covariance = sum([(x[i] - meanx) * (y[i] - meany) for i in range(n)])
correlation_coefficient = covariance / (n * std_dev_x * std_dev_y)
print(round(correlation_coefficient,3))