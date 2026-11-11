n=int(input())
bs = format(n, "b")
ibs=[int(c) for c in bs]
cnt=0
for i in range(len(ibs)):
    if ibs[i]==1:
        cnt=cnt+1
print(cnt)        