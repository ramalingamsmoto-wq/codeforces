s=input()
il=[int(c) for c in s]

mx=-1
#print(f"il {il}")

for i in range(len(il)):
    d=il[i]
    cnt=1
    for j in range(i+1,len(il),1):
        if il[j]==d:
            cnt+=1
        else:
            break 
    mx=max(mx,cnt) 
         
#print(f" mx {mx}")    

if mx >=7 :
    print("YES")  
else:
    print("NO")           