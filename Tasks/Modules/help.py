a=list(input())
b=list(input())
c=list(input())
d=list(input())
sl1=zip(a,b)
sl2=zip(b,a)
dic1 = {key:value for key,value in sl1}
dic2 = {key:value for key,value in sl2}
for x in c:
    print(dic1[x],end='')
print()
for y in d:
    print(dic2[y],end='')

