#!/usr/bin/python3
""" Rotate 2D Matrix """


def rotate_2d_matrix(matrix):
    """ Given an n x n 2D matrix,
    rotate it 90 degrees clockwise
    Do not return anything. The matrix must be edited in-place.
    You can assume the matrix will have 2 dimensions and will not be empty."""
    replica = matrix[:]

    for i in range(len(matrix)):
        column = [row[i] for row in replica]
        matrix[i] = column[::-1]
