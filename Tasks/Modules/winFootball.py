n=int(input())
d={}
for i in range(n):
    s = input().split(';')
    if s[0] not in d:
        d[s[0]]=[0,0,0,0,0]
    if s[2] not in d:
        d[s[2]]=[0,0,0,0,0]
    if s[1]==s[3]:
        d[s[0]][0]+=1
        d[s[0]][2]+=1
        d[s[0]][4] += 1
        d[s[2]][0]+=1
        d[s[2]][2]+=1
        d[s[2]][4] += 1
    elif int(s[1]) > int(s[3]):
        d[s[0]][0] += 1
        d[s[0]][1] += 1
        d[s[0]][4] += 3
        d[s[2]][0] += 1
        d[s[2]][3] += 1
    elif int(s[1])<int(s[3]):
        d[s[0]][0] += 1
        d[s[0]][3] += 1
        d[s[2]][4] += 3
        d[s[2]][0] += 1
        d[s[2]][1] += 1
for key, value in d.items():
    values_str = ' '.join(map(str, value))
    print(f"{key}:{values_str}")
