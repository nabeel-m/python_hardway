#!/bin/env python

def matrix(rows, cols):
    return [[int(input()) for i in range(cols)] for j in range(rows)]

# adds m1 and m2 if the dimensions match othewise returns [[]], False
def matrix_add(m1, m2):
    rows = len(m1)
    cols = len(m1[0])

    if rows != len(m2) or cols != len(m2[0]):
        return [[]], False

    result = [[0] * cols] * rows
    for i in range(rows):
        for j in range(cols):
            result[i][j] = m1[i][j] + m2[i][j]
    return result, True


def main():
    rows = int(input("rows    : "))
    cols = int(input("columns : "))
    m1 = matrix(rows, cols)
    print(m1)

    rows = int(input("rows    : "))
    cols = int(input("columns : "))
    m2 = matrix(rows, cols)
    print(m2)

    result, ok = matrix_add(m1, m2)
    if ok is False:
        print("Cannot add matrices")
        return 0

    print("sum of two matrixes:")
    print(result)
    return 0

if __name__ == '__main__':
    main()
