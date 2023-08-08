#!/usr/bin/python3
""" function that divides elements of a matrix"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given number
    Args:
        matrix (list): the matrix
        div (int or float): number to devide by
    Returns:
        list: A new matrix with elements devided by div and rounded off to 2dp
    """
    if type(matrix) != list or any(type(row) != list for row in matrix):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        n_row = [round(item / div, 2) for item in row]
        new_matrix.append(n_row)

    return new_matrix
