s=input()
sl=list(s)

i=0
vowels={"A","E","Y","I","O","U","a","e","y","i","o","u"}

while True:
    l=len(sl)
    
    if i>= l:
        break
        
    if sl[i] in vowels:
        sl.pop(i)
    else:
        if sl[i].isupper():
            c=sl[i]
            sl.pop(i)
            sl.insert(i,c.lower())
        sl.insert(i,".")
        i=i+2
        
res="".join(sl)  
print(res)    
           