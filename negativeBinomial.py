import math

def fac(a):
    if a == 0: return 1
    elif a== 1: return 1
    else: return (a*fac(a-1))

def prob(n, p, N, r):
    return (fac(n)/(fac(n-r+1)*fac(r-1))) * float(p**n)

def infoMeasure(n, p, N, r):
    return -1*float(math.log2(prob(n, p, N, r)))

def sumProb(N, p, r): 
    sum = 0.0
    for n in range(r, N+1):
        sum += prob(n, p, N, r)
    return sum

def approxEntropy(N, p, r):
    result = 0.0
    for n in range(r, N+1):
        key = prob(n, p, N, r)
        result += key*-1*infoMeasure(n, p, N, r)
    return result

#print(approxEntropy(5,0.3,1))