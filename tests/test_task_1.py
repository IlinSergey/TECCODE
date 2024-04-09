import pytest
from teccode.task_1 import unique_list


@pytest.mark.parametrize("numbers, expected_result", [
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([1, 1, 1, 1, 1], [1]),
    ([1, 1, 1, 1, 2], [1, 2]),
    ([-1, -1, -1, -1, -1], [-1]),
    ([], []),
]
)
def test__unique_list__success(numbers, expected_result):
    assert unique_list(numbers) == expected_result


@pytest.mark.parametrize("numbers, expected_result", [
    (1, "Only iterable objects are allowed!"),
    (unique_list, "Only iterable objects are allowed!"),
    ('string', "Only integer objects are allowed in the list!"),
    (None, "Only iterable objects are allowed!"),
])
def test__unique_list__fail(numbers, expected_result):
    assert unique_list(numbers) == expected_result
