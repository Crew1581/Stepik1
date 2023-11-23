a=[int(i) for i in input().split()]
c=0
if len(a)==1:
    print(a[0])
else:
    for i in range(len(a)-1):
        c=a[-1+i]+a[i+1]
        print(c, end=' ')
    print(a[-2]+a[0])