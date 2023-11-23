s=[int(i) for i in input().split()]
a=int(input())
b=0
for i in range(len(s)):
    if s[i]==a:
        print(i, end=' ')
        b+=1
if b==0:
    print('Отсутствует')

