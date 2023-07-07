#!/usr/bin/python3
"""
Module contains lazy_matrix_mul function
"""


def lazy_matrix_mul(m_a, m_b):
    """ multiplies 2 matrices using numpy module"""
    import numpy as np

    return np.dot(m_a, m_b).tolist()
