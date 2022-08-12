
maths = [95,85,80,70,60]
stats = [85,95,70,65,70]

def find_coeff_b(x,y):
    n = len(x)
    xy =[x[i]*y[i] for i in range(n) ]
    x_square = [i**2 for i in x]
    b = (n*(sum(xy))-((sum(x)*sum(y))))/float(((n*sum(x_square))-sum(x)**2))
    return b
    
def find_coeff(x,y):
    x_mean = sum(x)/float(len(x))    
    y_mean = sum(y)/float(len(y))
    b = find_coeff_b(x,y)
    a = y_mean - b*x_mean
    return a,b
    
a,b = find_coeff(maths,stats)
print (a + b*80)