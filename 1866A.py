n=int(input())
a=list(map(int,input().strip().split()))
limit=(10**9)
ne=[-limit]
pe=[limit]
ze=[]



for e in a:
    if e==0:
        ze.append(e)
    elif e >0:
        pe.append(e)
    elif e < 0:
        ne.append(e) 
if len(ze)>0:
    print(0)   
else:
    print(min(abs(max(ne)),min(pe)))               
