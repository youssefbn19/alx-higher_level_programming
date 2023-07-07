#!/usr/bin/python3
"""
Module contains matrix_mul function
"""


def matrix_mul(m_a, m_b):
    """ multiplies 2 matrices """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    elif type(m_b) is not list:
        raise TypeError("m_b must be a list")
    elif not all(type(ele) is list for ele in m_a):
        raise TypeError("m_a must be a list of lists")
    elif not all(type(ele) is list for ele in m_b):
        raise TypeError("m_b must be a list of lists")
    elif not m_a or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    elif not m_b or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    elif not all(type(col) in [int, float] for row in m_a for col in row):
        raise TypeError("m_a should contain only integers or floats")
    elif not all(type(col) in [int, float] for row in m_b for col in row):
        raise TypeError("m_b should contain only integers or floats")
    elif not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    elif not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    elif len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    m_p = []
    for z in range(len(m_a)):
        new_row = []
        for j in range(len(m_b[0])):
            mult = 0
            for i in range(len(m_a[0])):
                mult += m_a[z][i] * m_b[i][j]
            new_row += [mult]
        m_p += [new_row.copy()]

    return m_p
