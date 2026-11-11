
def process(s):
    size=len(s)
    tans=s
    if size > 10:
        tans=s[0]+str(size-2)+s[size-1]
    return tans    




t=int(input())
res=[]
for _ in range(t):
    s=input()
    res.append(process(s))
for e in res:
    print(f"{e}")    