import math

def process(n, k, a):
    aux = [-1] * n
    evens = 0
    for i in range(n):
        e = a[i]
        if e % 2 == 0:
            evens += 1
            
        if a[i] % k == 0:
            aux[i] = 0
        else:
            q = math.ceil(a[i] / k)
            v1 = (q * k) - a[i]
            aux[i] = v1
            
    r = min(aux)
    
    if k == 4:
        r = min(r, max(0, 2 - evens))
        
    return r            


t = int(input())
res = []
for i in range(t):
    n, k = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    tans = process(n, k, a)
    res.append(tans)
for e in res:
    print(e)
    