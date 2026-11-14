n=input()
if len(n)==1:
    print(str(n))
else:
    a=list(map(int,n.strip().split("+")))
    a.sort()
    res=str(a[0])
    for i in range(1,len(a),1):
        res=res+ "+"+str(a[i])
    res=res.strip()    
    print(res)        