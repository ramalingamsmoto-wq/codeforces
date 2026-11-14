n=int(input())
v=0
for i in range(n):
    s=input()
    if s[0]=='+' or s[-1]=='+':
        v=v+1
    if s[0]=='-' or s[-1]=='-':
        v=v-1    
print(v)        