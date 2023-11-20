a=int(input())
b=int(input())
s=0
c=0
for i in range(a,b+1):
    if i % 3 == 0:
        c+=1
        s+=i

print(s/c)