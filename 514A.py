x=int(input())
sx=str(x)
il=[int(c) for c in sx]
iil=[9-e for e in il]
l=len(il)
rl=[0]*l
rs=""
for i in range(l):
    rl[i]=min(il[i],iil[i])
    rs=rs+str(rl[i])
    
    if i==l-1 and int(rs)==0:
        for j in range(l):
            if il[j]==9:
                rs="9"+("0"*(l-j-1))
                break
        
            
    
    

res=int(rs)
print(res)


