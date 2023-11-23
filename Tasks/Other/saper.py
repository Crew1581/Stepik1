n, m, k = (int(i) for i in input().split()) # строки, столбцы, кол-во мин
a = [[0 for j in range(m)] for i in range(n)] # пустая таблица из 0
for i in range(k):  # перебираем кол-во мин
    rw, cl = (int(i) - 1 for i in input().split()) # записываем строку и столбец одной мины при каждом проходе
    a[rw][cl] = -1 # записываем мину по координатам столбца и колонны
for i in range(n): # перебираем строки
    for j in range(m): # перебираем столбцы
        if a[i][j] == 0: # ячейка без мины
            for di in range(-1, 2): # перебираем соседние строки (просто цифры -1 0 1)
                for dj in range(-1, 2):  # перебираем соседние столбцы (просто цифры -1 0 1)
                    ai = i + di   # координата по строке
                    aj = j + dj   # координата по столбцу
                    if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1: # проверка вхождения в диапазон и мины по соседству
                        a[i][j] += 1
for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            print('*', end='')
        elif a[i][j] == 0:
            print('.', end='')
        else:
            print(a[i][j], end='')
    print()