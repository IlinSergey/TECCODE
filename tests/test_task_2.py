import pytest
from teccode.task_2 import prime_numbers


@pytest.mark.parametrize("min_num, max_num, expected_result", [
    (1, 10, [2, 3, 5, 7]),
    (1, 100, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]),
])
def test__prime_numbers__success(min_num, max_num, expected_result):
    assert prime_numbers(min_num, max_num) == expected_result


@pytest.mark.parametrize("min_num, max_num", [
    (-1, 10),
    (10, -1),
    (-1, -1),
    (10, 5),
    (10, 'string'),
    ('string', 10),
    (10, None),
])
def test__prime_numbers__fail(min_num, max_num):
    with pytest.raises(ValueError):
        prime_numbers(min_num, max_num)
