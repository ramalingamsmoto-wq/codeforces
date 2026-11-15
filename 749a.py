n=int(input())
ans=[]
if n%2==0:
    q=n//2
    ans=[2]*q
else:
    q=n//2
    q=q-1
    ans=[2]*q
    ans.append(3)
print(len(ans))   
print(*ans)     