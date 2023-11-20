a=input()
s=1
a=a+'0'
for j in range (0,len(a)-1):
    if a[j]==a[j+1]:
     s+=1
    else:
     print((a[j]+str(s)),end='')
     s=1