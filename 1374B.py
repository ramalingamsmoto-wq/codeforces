limit = (2**70)    
mn = limit   

def process1(n, moves):
    global mn
    if n == 1:
        mn = min(mn, moves) 
    elif n % 6 == 0:
        process1(n // 6, moves + 1) 
    elif n % 6 != 0 and n % 3 == 0:
        process1(n * 2, moves + 1)
        
    if mn == limit:
        return -1
            
    return mn              

t = int(input())
res = []
for _ in range(t):
    n = int(input())
    mn = limit  # 🔥 CRITICAL FIX: Reset mn to infinity for every new test case
    tans = process1(n, 0)
    res.append(tans)

for e in res:
    print(e)    
    