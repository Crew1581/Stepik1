c = []
while True:
    a = [i for i in input().split()]
    if a == ['end']:
        break
    c.append(a)
n, m = len(c), len(c[0])
for i in range(n):
    for j in range(m):
        x = int(c[i][j-1]) + int(c[i][j+1-m]) + int(c[i-1][j]) + int(c[i+1-n][j])
        print(x, end=' ')
    print()