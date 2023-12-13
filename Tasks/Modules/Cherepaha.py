d={}
sl=[]
n=int(input())
c1=0
c2=0
c3=0
c4=0
for i in range(n):
    s = input()
    s=s.split()
    sl.append(s)
    if sl[i][0] in d:
        #print(d[s[i][0]])
        d[sl[i][0]]+= int(sl[i][1])
        #print(d)
    elif sl[i][0] not in d:
        d[sl[i][0]] = int(sl[i][1])

for key, value in d.items():
    if key=='север':
        c1+=value
    elif key=='юг':
        c2+=value
    elif key=='запад':
        c3+=value
    elif key=='восток':
        c4+=value
print(c4-c3, c1-c2)