"""Tests for the CSS row-space intersection diagnostic."""
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

from qldpc_verify import css_row_space_intersection_dimension  # noqa: E402


def dim(hx, hz):
    return css_row_space_intersection_dimension(
        np.asarray(hx, dtype=np.uint8), np.asarray(hz, dtype=np.uint8)
    )


def test_known_intersection_dimension():
    # row(HX)=<e0,e1>, row(HZ)=<e1,e2>; the intersection is <e1>.
    assert dim([[1, 0, 0], [0, 1, 0]],
               [[0, 1, 0], [0, 0, 1]]) == 1


def test_disjoint_and_identical_row_spaces():
    assert dim([[1, 0, 0]], [[0, 1, 0]]) == 0
    assert dim([[1, 0, 1], [0, 1, 1]],
               [[1, 0, 1], [0, 1, 1]]) == 2


def test_generator_basis_and_redundancy_do_not_change_it():
    hx = [[1, 0, 1, 0], [0, 1, 1, 0]]
    hz = [[1, 1, 0, 0], [0, 0, 0, 1]]
    expected = dim(hx, hz)
    # Replace the second X generator by its XOR with the first, then add
    # duplicate/dependent rows. The generated row spaces are unchanged.
    hx2 = [[1, 0, 1, 0], [1, 1, 0, 0],
           [1, 0, 1, 0], [0, 1, 1, 0]]
    assert dim(hx2, hz) == expected


def test_qubit_permutation_does_not_change_it():
    hx = np.asarray([[1, 0, 1, 0], [0, 1, 1, 0]], dtype=np.uint8)
    hz = np.asarray([[1, 1, 0, 0], [0, 0, 0, 1]], dtype=np.uint8)
    permutation = [2, 0, 3, 1]
    assert css_row_space_intersection_dimension(hx, hz) == (
        css_row_space_intersection_dimension(hx[:, permutation], hz[:, permutation])
    )


def test_global_x_z_exchange_does_not_change_it():
    hx = [[1, 0, 1, 0], [0, 1, 1, 0]]
    hz = [[1, 1, 0, 0], [0, 0, 0, 1]]
    assert dim(hx, hz) == dim(hz, hx)


def test_equal_dimension_is_not_an_equivalence_claim():
    # These pairs have the same scalar invariant (zero) but visibly different
    # row-space dimensions. Equality of the diagnostic is deliberately only a
    # necessary screen, never a certificate of equivalence.
    assert dim([[1, 0, 0]], [[0, 1, 0]]) == 0
    assert dim([[1, 0, 0], [0, 1, 0]], [[0, 0, 1]]) == 0
