import pytest
from teccode.task_4 import sort_list_by_length


@pytest.mark.parametrize("strings, expected_result", [
    (["abc", "def", "ghi"], "['abc', 'def', 'ghi']\n['abc', 'def', 'ghi']\n"),
    (["a", "de", "ghi", "jklm"], "['a', 'de', 'ghi', 'jklm']\n['jklm', 'ghi', 'de', 'a']\n"),
    (["abc", "d", "gh", "jklm"], "['d', 'gh', 'abc', 'jklm']\n['jklm', 'abc', 'gh', 'd']\n"),
])
def test__sort_list_by_length__success(capfd, strings, expected_result):
    sort_list_by_length(strings)
    out, err = capfd.readouterr()
    assert out == expected_result


@pytest.mark.parametrize("strings, error", [
    ([1, 2, 3], ValueError),
])
def test__sort_list_by_length__fail(strings, error):
    with pytest.raises(error):
        sort_list_by_length(strings)


def test__sort_list_by_length__type_error():
    assert sort_list_by_length(None) == "Only iterable objects are allowed!"
    assert sort_list_by_length(123) == "Only iterable objects are allowed!"
