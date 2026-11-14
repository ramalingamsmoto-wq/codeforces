

def process(x,k):
    tup=()
    if x%k!=0:
        tup=(1,[x])
    else:
        for i in range(1,x,1):
            if i%k!=0 and (x-i)%k!=0:
                tup=(2,[i,x-i])
                break
    return tup                
        


t=int(input())
res=[]
for _ in range(t):
    x,k=map(int,input().strip().split())
    tans=process(x,k)
    res.append(tans)
for tup in res:
    print(tup[0])
    a=tup[1]
    print(a[0],end='')   
    for j in range(1,len(a),1):
        print(" "+str(a[j]),end='')
    print()    