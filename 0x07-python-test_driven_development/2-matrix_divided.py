#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
        return matrix
    elif div == 0:
        raise ZeroDivisionError("division by zero")
        return matrix

    row_len = -1
    new = []
    for row in matrix:
        if (row_len != len(row) and row_len != -1):
            raise TypeError("Each row of the matrix must have the same size")
            return matrix
        for ele in row:
            if not isinstance(ele, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of" +
                                " integers/floats")
                return matrix
            else:
                new.append(round(ele / div, 2))
        row_len = len(row)

    return new
