a = int(input())
b = int(input())
c = int(input())
d = int(input())
l1 = b - a
l2 = d - c
print('\t', end='')
for k in range(l2+1):
    c1=c+k
    print(c1, end='\t')
print()
for i in range(l1+1):

    for j in range(l2+2):
        if j ==0:
            print(a, end='\t')
        else:
            print(a*(c+j-1), end='\t')
    a=a+1
    print()