cnt=0
i=1
aux=[-1]
while True:
    if cnt==1001:
        break
    elif i%3 !=0 and i%10 !=3 :
        #print(f"i {i}")
        aux.append(i)  
        cnt=cnt+1 
    i=i+1     

t=int(input())
res=[]
for _ in range(t):
    k=int(input())
    res.append(aux[k])
for e in res:
    print(e)    