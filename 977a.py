n,k= map(int,input().strip().split())

i=1
while i <=k :
    
    rem=n%10
    if rem==0:
        n=n//10
    else:
        n=n-1   
    
    i=i+1
print(n)    