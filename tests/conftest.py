import pytest
from teccode.task_3 import Point


@pytest.fixture
def point_1():
    return Point(0, 0)


@pytest.fixture
def point_2():
    return Point(3, 4)
