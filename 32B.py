s=input()
sl=list(s)
rl=[]

i=0
l=len(sl)
while True:
    if i>=l:
        break
        
    if sl[i]=='.':
        rl.append('0')
        i=i+1
    elif sl[i]=='-':
        i=i+1
        if sl[i]  =='-':
            rl.append('2')
        elif sl[i] =='.':
            rl.append('1')
        i=i+1        

rs="".join(rl)
print(rs)    