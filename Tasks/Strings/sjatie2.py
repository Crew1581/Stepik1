s = input()
s1 = ""
a = 0
b = s[0]
for i in s:
    if i == b:
        a += 1
    else:
        s1 += b + str(a)
        a = 1
        b = i
s1 += b + str(a)
print(s1)