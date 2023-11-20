s=input()
c=1
q=''
if len(s)==1:
    q=q+s[0]+str(c)
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        c+=1
        if i==len(s)-2:
            q=q+s[i]+str(c)
    elif s[i]!=s[i+1]:
        q=q+s[i]+str(c)
        c=1
        if i==len(s)-2:
            q=q+s[i+1]+str(c)
    else:
        q=q+s[i]+str(c)
print(q)
