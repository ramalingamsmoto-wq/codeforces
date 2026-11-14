from collections import Counter


def process(n,a):
    tup=()
    a.sort()
    counts = Counter(a)
    
    all_equal = all(x == a[0] for x in a)
    if all_equal:
        tup=(-1,)
    else:
        cnt=counts[a[0]]
        b=[a[0]]*cnt
        c=a[cnt:]
        tup=(len(b),b,len(c),c) 
       # print(f"tup {tup}")
    return tup      

        


t=int(input())
res=[]
for _ in range(t):
    n=int(input())
    a=list(map(int,input().strip().split()))
    tans=process(n,a)
    res.append(tans)
for tup in res:
    if tup[0] == -1:
        print(-1)
    else:    
        print(str(tup[0])+ " "+str(tup[2]))
        b=tup[1]
        c=tup[3]
        print(b[0],end='')   
        for j in range(1,len(b),1):
            print(" "+str(b[j]),end='')
        print()
        print(c[0],end='')   
        for j in range(1,len(c),1):
            print(" "+str(c[j]),end='')
        print()
       