s = []
sr=0
d = {g: [0, 0] for g in range(1, 12)}

with open('C:\\Python_Course\\Text.txt', "r", encoding='utf-8') as f:
    for line in f:
        strk = line.strip()
        st = strk.split('\t')
        s.append(st)
print(s)
for i in range(len(s)):
    if int(s[i][0]) in d:
        #print(d[s[i][0]])
        d[int(s[i][0])][0]+= int(s[i][2])
        d[int(s[i][0])][1]+=1
        #print(d)
    elif s[i][0] not in d:
        d[int(s[i][0])] = [int(s[i][2]),1]
print(d)
fr = open('C:\\Python_Course\\answ.txt', 'w')
from collections import OrderedDict
od = OrderedDict(sorted(d.items()))

# Выводим значения упорядоченного словаря
for key, value in od.items():
    if value[0]!=0:
        fr.write(f'{key} {value[0]/value[1]} \n')
    else:
        fr.write(f'{key} {'-'} \n')
