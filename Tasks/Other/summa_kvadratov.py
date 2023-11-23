c=0
s=0
while True:
    a=int(input())
    c+=a
    s+=a**2
    if c==0:
        print(s)
        break