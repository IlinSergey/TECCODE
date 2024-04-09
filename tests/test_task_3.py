
def test__point__distance(point_1, point_2):
    assert point_1.distance(point_2) == 5


def test__point__set_coordinates(point_1):
    point_1.set_coordinates = (1, 2)
    assert point_1.coordinates == (1, 2)


def test__point__get_coordinates(point_1, point_2):
    assert point_1.coordinates == (0, 0)
    assert point_2.coordinates == (3, 4)


def test__point__init(point_1):
    assert point_1.x == 0
    assert point_1.y == 0
