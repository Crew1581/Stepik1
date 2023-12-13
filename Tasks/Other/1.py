f= open('C:\\Python_Course\\Text.txt','r')
s=[]
for line in f:
    str=line.lower().strip()
    st = str.split()
    for i in range(len(st)):
        s.append(st[i])

#print(s)

c=0
s.sort()
#print(s)
d={}
for i in range(len(s)):
    if s[i] in d:
        d[s[i]] += 1
    elif s[i] not in d:
        d[s[i]] = 1
c=max(d.values())
for key, value in d.items():
    if value==c:
        print(key,value)
        c+=1
