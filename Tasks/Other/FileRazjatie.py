f= open('C:\\Python_Course\\Text.txt','r')
st=f.readline().strip()
c=0
s=[]
print(len(st))
for i in range(len(st)-1):
    if st[i]>='A' and st[i+1]<'A':
        s.append(st[i])
    elif st[i]<'A' and st[i+1]>='A' and st[i-1]>='A':
        for j in range(int(st[i])-1):
            s.append(st[i-1])
    elif st[i]<'A' and st[i+1]<'A':

        for j in range(int(st[i]+st[i+1])-1):
            s.append(st[i-1])
            c+=1
            print(c)
if st[-1]!=1 and st[-2]>='A':
    for j in range(int(st[-1]) - 1):
        s.append(st[- 2])
fr = open('C:\\Python_Course\\answ.txt', 'w')

for g in range(len(s)):
    print(s[g],end='')
    fr.write(s[g])

