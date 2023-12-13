n=int(input())
sl=[]
sent=[]
checker=[]
for i in range(n):
    s=input()
    s=s.lower()
    sl.append(s)
sl = set(sl)
k = int(input())
for j in range(k):
    sen = input().lower().split()
    sent+=sen
for x in sent:
    if x not in sl and x not in checker:
        checker+=x.split()
        print(x)
