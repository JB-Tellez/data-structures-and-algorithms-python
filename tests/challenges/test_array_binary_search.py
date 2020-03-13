from data_structures_and_algorithms.challenges.array_binary_search.array_binary_search import (
    binary_search,
)


def test_find_15_at_2():
    actual = binary_search([4, 8, 15, 16, 23, 42], 15)
    expected = 2
    assert actual == expected


def test_do_not_find_90():
    actual = binary_search([11, 22, 33, 44, 55, 66, 77], 90)
    expected = -1
    assert actual == expected
