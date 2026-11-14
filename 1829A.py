
def process(s):
    t="codeforces"
    cnt=0
    for i in range(len(t)):
        if t[i] != s[i]:
            cnt+=1
    return cnt        

t=int(input())
res=[]
for i in range(t):
    s=input()
    tans=process(s)
    res.append(tans)
for e in res:
    print(e)    