s=input()
nl=[int(c) for c in s]
cnt=0
for i in range(len(nl)):
    if nl[i] ==4 or nl[i] ==7:
        cnt=cnt+1
if cnt==7 or cnt == 4:
    print("YES")  
else:
    print("NO")          