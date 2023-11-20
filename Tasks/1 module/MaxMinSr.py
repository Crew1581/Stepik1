a = int(input())
b = int(input())
c = int(input())
if a >= b and a >= c:
    ma = a
    if b > c:
        mi = c
        sr = b
    else:
        mi = b
        sr = c
elif b >= a and b >= c:
    ma = b
    if a > c:
        mi = c
        sr = a
    else:
        mi = a
        sr = c
elif c >= a and c >= b:
    ma = c
    if a > b:
        mi = b
        sr = a
    else:
        mi = a
        sr = b
print(ma)
print(mi)
print(sr)