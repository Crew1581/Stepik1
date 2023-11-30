n=int(input())
matrix = [[0] * n for _ in range(n)]

top, bottom, left, right = 0, n - 1, 0, n - 1
direction = 0  # 0: вправо, 1: вниз, 2: влево, 3: вверх

num = 1

while top <= bottom and left <= right:
    if direction == 0:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1
    elif direction == 1:
        for i in range(top, bottom + 1):
             matrix[i][right] = num
             num += 1
        right -= 1
    elif direction == 2:
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1
    elif direction == 3:
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

    direction = (direction + 1) % 4



# Вывод матрицы
for i in range(n):
    for j in range(n):
      print(matrix[i][j], end=' ')
    print()