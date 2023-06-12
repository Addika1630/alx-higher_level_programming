#!/usr/bin/python3

"""Matrix multiplication with NumPy install library."""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Matrix multiplication of two matrices

    Args:
       m_a: the dirst matrices
       m_b: the second matrices

    Return:
        New multiplied matrix
    """

    result = np.matmul(m_a, m_b)

    return (result)
