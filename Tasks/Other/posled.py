a=int(input())
b=[]
c=[1]
for i in range(a):
    b=b+[i+1]*(i+1)
for j in range(a):
    print(b[j], end=' ')