d={}
n=int(input())
xi=[]
for j in range(n):
    xi.append(input())
for i in range(n):
    #xi=int(input())
    if xi[i] in d:
        print(d[xi[i]])
    elif xi[i] not in d:
        d[xi[i]] = f(int(xi[i]))
        print(d[xi[i]])