import math 
#1a

def prob(n, p):
    return p**n

def infoMeasure(n, p):
    return (-1) * float( math.log2(prob(n,p)) )

def sumProb(N, p):
    sum=0
    for n in range(1, N+1):
        sum+=prob(n, p)
    return sum

"""
hàm sumProb là tổng của cấp số nhân lùi hữu hạn( vô hạn phụ thuộc vào giá trị N)
nên giá trị sum sẽ có lim là 1 
"""
def  approxEntropy(N,p):
    a = 0.0
    for n in range(1, N+1):
        key = prob(n, p)
        a += key*math.log2(key)*(-1)
    return a

print(approxEntropy(5,0.33))