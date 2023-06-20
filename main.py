# ✔Напишите функцию для транспонирования матрицы
import  random
import random

SIZE_W = 5
SIZE_H = 5

matrix = [[0 for x in range(SIZE_W)] for y in range(SIZE_H)]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        matrix[i][j] = random.randint(0, 20)


def my_func(my_matrix: list) -> list:
    matrix_transport = [[0 for x in range(len(my_matrix))] for y in range(len(my_matrix[0]))]
    for i in range(len(my_matrix)):
        for j in range(len(my_matrix[0])):
            matrix_transport[j][i] = my_matrix[i][j]

    return matrix_transport


print(my_func(matrix))
# ✔Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.

# ✔Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно сохраняйте все операции поступления и снятия средств в список.