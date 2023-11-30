str = input().lower().split()
d={}
for i in range(len(str)):
    if str[i] in d:
        d[str[i]] += 1
    elif str[i] not in d:
        d[str[i]] = 1
for key, value in d.items():
    print(key, value)
#s = input().lower().split()
#for i in set(s):
#    print(i, s.count(i))