# Напишите функцию для транспонирования матрицы
from copy import deepcopy


def transp_matrix(matrix):
    transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    # for i in range(len(matrix)):
    #     for j in range(len(matrix[0])):
    #         transposed[j][i] = matrix[i][j]
    return transposed


matrix = [[1, 4, 5],
          [3, 5, 7]]
print(transp_matrix(matrix))
