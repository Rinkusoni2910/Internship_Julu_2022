import math
def cdf(max_Wt, mean_wt, std_dev):
    Z = (max_Wt - mean_wt)/std_dev
    return 0.5*(1 + math.erf(Z/(math.sqrt(2))))

max_Wt = int(input())
size = int(input())
mean_wt = int(input())
std_dev = int(input())

mean_wt_sum = size * mean_wt
std_dev_sum = math.sqrt(size) * std_dev


print(round(cdf(max_Wt, mean_wt_sum, std_dev_sum), 4))