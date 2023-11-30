def f(x):
    if x<=-2:
        y=1-(x+2)**2
        return y
    elif x>-2 and x<=2:
        y=-x/2
        return y
    elif x>2:
        y=(x-2)**2+1
        return y
x=float(input())
print(f(x))