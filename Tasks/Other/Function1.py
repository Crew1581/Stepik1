def my_range(start, stop, step = 1):
    r = []
    for i in range(start, stop + 1, step):
        r.append(i)
    return r
print(my_range(15, 2, -2))