import math 

#1b
"""
  n: là symbol mà ta đang cần tính xác suất (chính là k, và prob(...) chính là p(k)
  p: tham số, là xác suất của phép thử bernoulli (phép tung xu) tương ứng
  N: Tổng số xu được tung (tổng số phép thử bernoulli)
"""
def fac(a):
    if a == 0: return 1
    elif a== 1: return 1
    else: return (a*fac(a-1))

def prob(n,p,N):
    b= fac(N)/(fac(n)*fac(N-n))
    return b * (p**n) * ((1-p)**(N-n))

def infoMeasure(n, p, N):
    return -1*float(math.log2(prob(n, p, N)))
#print (infoMeasure(1,0.3,5))

def sumProb(N, p):
    a=0
    for i in range(1,N):
        a += prob(i,p,N)
    return a
# print (sumProb(5, 0.2))

"""
hàm sumProb là tổng của cấp số nhân lùi hữu hạn( vô hạn phụ thuộc vào giá trị N)
theo công thức tính tổng cấp số nhân lùi vô hạn ta tính được giá trị của sum sẽ có lim=1.
"""

def approxEntropy(N, p):
    result = 0.0
    for n in range(1, N+1):
        key = prob(n, p, N)
        result += key*-1*infoMeasure(n, p, N)
    return result

#print( approxEntropy(5, 0.5) )





