n,m=map(int,input().strip().split())
d=dict()
vl=dict()
res=[]
for i in range(n):
    sm=list(map(int,input().strip().split()))
    seq=sm[1:]
    d[i]=sm
    for e in seq:
        if e not in vl:
            vl[e]={i}
        else:
            vl[e].add(i)   
mx=max(d)
us=set()      
for i in range(mx+1):
    us.add(i)   
        
for j in range(m):
    qm=list(map(int,input().strip().split()))
    q=qm[1:]
    aux=[]
    for e in q:
        if e > 0:
            aux.append(vl[e])
        else:
            e=-e
            v1=vl[e]
            v2=us.difference(v1)
            aux.append(v2)    
            
    rs=aux[0]
    for i in range(1,len(aux),1):
        rs=rs.intersection(aux[i])
    rl=list(rs)
    rl.sort()
    tup=(len(rl),rl)
    res.append(tup)
for tup in res:
    print(tup[0])
    for seqid in tup[1]:
        v1=d[seqid]
        print(*v1)    
        