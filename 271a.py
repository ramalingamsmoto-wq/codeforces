n=input()

ni=int(n)
ni=ni+1

while True:
    sni=str(ni)
    l=len(sni)
    hs=set(sni)
    dl=len(hs)
    if l==dl:
        ans=ni
        break
    else:
        ni=ni+1 
           
print(ans)