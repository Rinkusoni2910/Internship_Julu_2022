import math
def cdf(Ticket, mean_purchase, std_dev):
    Z = (Ticket - mean_purchase)/std_dev
    return 0.5*(1 + math.erf(Z/(math.sqrt(2))))

Ticket = int(input())
Waiting_stu = int(input())
mean_purchase = float(input())
std_dev = float(input())

mean_purchase_sum = Waiting_stu * mean_purchase
std_dev_sum = math.sqrt(Waiting_stu) * std_dev


print(round(cdf(Ticket, mean_purchase_sum, std_dev_sum), 4))