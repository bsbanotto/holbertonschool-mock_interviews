#!/usr/bin/python3
"""
Square every value of a matrix
"""


def square_matrix(matrix):
    newmatrix = []
    for row in matrix:
        newlist = []
        for column in row:
            newlist.append(column * column)
        newmatrix.append(newlist)

    return newmatrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix(matrix)
print(new_matrix)
print()
print(matrix)
