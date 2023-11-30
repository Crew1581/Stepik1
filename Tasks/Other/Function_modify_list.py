def modify_list(l):
    ls=[]
    lsH=[]
    i=0
    ls.extend(l)
    lsH.extend(l)
    l.clear()
    #print(ls)
    for x in ls:
        #print(x)
        if x%2==0:

            y=x//2
            l.append(y)
        if x%2!=0:
            lsH.remove(x)

lst=[1,2,3,4,5,6,7,8,8,10,12]
print(modify_list(lst))
print(lst)
modify_list(lst)
print(lst)