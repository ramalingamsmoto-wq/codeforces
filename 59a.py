s=input()
uc=0
lc=0
sl=list(s)
l=len(sl)

for i in range(len(sl)):
    if sl[i].isupper():
        uc+=1
    else:
        lc+=1
#print(f"uc {uc} lc {lc}")        
if lc==uc:
    res=s.lower()
elif uc< lc:
    res=s.lower()
else:
    res=s.upper() 
print(res)       
                    