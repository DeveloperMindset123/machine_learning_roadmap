""" """

import math
import random
from typing import List, Optional, Union, Tuple

# special shape data type to return the rows and columns of an array

Shape = Union[int, Tuple(int, int)]


def vector(data):
    """
     Scope: 1-D array constructor — the np.array equivalent, restricted to vectors.
    Mirrors: np.array(data) for 1-D input.

    Take a flat list/iterable of numbers and return your internal vector
    representation (decision to make: a plain list, or a Vector object).

    Validate: input is 1-D (reject a list-of-lists — that case belongs to
    from_nested_list); all elements numeric. Decide behavior on empty input.
    Out of scope for now: dtype (assume float), N-D.
    """

    return list(data)


def full(shape: Shape, value):  # type: ignore
    """
    scope: constant-filled array - the base builder that zeros/ones delegate to.
    Mirros: np.full(shape, value)

    Accept shape as an int (-> 1_D vector of lenght n) or a 2-tuple (m,n)

    (-> m x n matrix). Return that structure with every entry set to `value`

    Build this one clenly first: then zeros and ones ecome one-liners on top of it (composition - first reuse decision?)

    edge: 0 dimensions -> empty:reject negative dims.
    """
    if type(shape) == int:
        full_arr = []
        for _ in range(0, shape):
            full_arr.append(value)

    else:
        """we encounter a tuple in this case"""
        """retrieve the column, insert the value, derement row by 1"""
        inner_element_arr = []
        ans = [[]]
        for _ in range(shape[1]):
            """same logic as the above if statement in this case"""
            inner_element_arr.append(value)

        for _ in range(shape[0]):
            ans.append(inner_element_arr)

        return ans


def zeros(n):
    """ """
    pass


def ones(n: List[int]):
    pass


def eye(n):
    pass


def from_nested_list():
    pass


def shape(n):
    pass


def random_matrix(m, n):
    """implement np.random, replication logic, in pure python"""
    pass


def reshae(x, new_shape):
    pass
