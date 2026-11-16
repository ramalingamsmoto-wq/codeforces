from collections import Counter

res=[]
for _ in range(int(input())):
    a=input()
    counts=Counter(a)
    if counts['A'] >= counts['B']:
        res.append('A')
    else:
        res.append('B')   
        
for e in res:
    print(e)         