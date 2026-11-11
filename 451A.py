
n,m=map(int,input().strip().split())

moves=0

while True:
    if n>0 and m>0:
        moves=moves+1
        n=n-1
        m=m-1
    else:
        break    
        

if moves%2==0:
    print("Malvika")
else:
    print("Akshat")    