n=int(input())
s=input()
sl=list(s)

i=1
cnt=0
while True:
    l=len(sl)
    if i >= l:
        break
    if sl[i]==sl[i-1]:
        sl.pop(i)
        cnt=cnt+1
    else:
        i=i+1    
print(cnt)    
    