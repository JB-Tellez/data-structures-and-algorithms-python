from data_structures_and_algorithms.challenges.array_shift.array_shift import (
    array_shift,
)


def test_shift_when_even():
    actual = array_shift([2, 4, 6, 8], 5)
    expected = [2, 4, 5, 6, 8]
    assert actual == expected


def test_shift_when_odd():
    actual = array_shift([4, 8, 15, 23, 42], 16)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected
