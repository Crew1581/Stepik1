matrix = []
matrix_s= []
while True:
    row_input = input()

    # Проверяем, завершил ли пользователь ввод
    if row_input == 'end':
        break

    # Разделяем строку на элементы  `
    row = [int(element) for element in row_input.split()]
    # Добавляем строку в матрицу
    matrix.append(row)
matrix_s=[[0]*len(matrix[0]) for g in range(len(matrix))]
# Вывод матрицы
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
            if j<len(matrix[0])-1 and i<len(matrix)-1 and j>0 and i>0 :
                matrix_s[i][j] = matrix[i - 1][j] + matrix[i + 1][j] + matrix[i][j - 1] + matrix[i][
                    j + 1]
            elif j==len(matrix[0])-1 and i!=len(matrix)-1:
                matrix_s[i][j] = matrix[i - 1][j] + matrix[i + 1][j] + matrix[i][j-1] + matrix[i][
                    0]
            elif j!=len(matrix[0])-1 and i==len(matrix)-1:
                matrix_s[i][j] = matrix[i - 1][j] + matrix[0][j] + matrix[i][j + 1] + matrix[i][
                    j - 1]
            elif i==len(matrix)-1 and j==len(matrix[0])-1:
                matrix_s[i][j] = matrix[i - 1][j] + matrix[0][j] + matrix[i][j-1] + matrix[i][
                    0]

            elif j==0 and i!=0:
                matrix_s[i][j] = matrix[i - 1][j] + matrix[i + 1][j] + matrix[i][j + 1] + matrix[i][
                    -1]
            elif j!=0 and i==0:
                matrix_s[i][j] = matrix[-1][j] + matrix[i + 1][j] + matrix[i][j + 1] + matrix[i][
                    j - 1]
            elif i==0 and j==0:
                matrix_s[i][j] = matrix[-1][j] + matrix[i + 1][j] + matrix[i][j + 1] + matrix[i][
                    -1]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      print(matrix_s[i][j], end=' ')
    print()