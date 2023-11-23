a=[int(i) for i in input().split()]
a.sort()
c=0
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        c+=1
        if a[i]==a[-1] and i==len(a)-2:
            print(a[i])
    elif a[i]!=a[i+1] and c>0:
        print(a[i], end=' ')
        c=0