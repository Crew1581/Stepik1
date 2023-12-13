s = []
sr=0
mat=0
fiz=0
rus=0

with open('C:\\Python_Course\\Text.txt', "r", encoding='utf-8') as f:
    for line in f:
        strk = line.strip()
        st = strk.split(';')
        s.append(st)



fr = open('C:\\Python_Course\\answ.txt', 'w')
for x in s:
    sr = (int(x[1]) + int(x[2]) + int(x[3])) / 3
    mat += int(x[1])
    fiz += int(x[2])
    rus += int(x[3])
    fr.write(str(sr) + '\n')
    #print(str(sr))
mat/=len(s)
fiz/=len(s)
rus/=len(s)

fr.write(str(mat))
fr.write(' ')
fr.write(str(fiz))
fr.write(' ')
fr.write(str(rus))
