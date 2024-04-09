from math import sqrt


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def distance(self, other: "Point") -> float:
        """
        Calculate the distance between two points.

        Parameters:
            other (Point): The other point to calculate the distance from.

        Returns:
            float: The distance between the two points.
        """
        dist = sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        return dist

    @property
    def coordinates(self) -> tuple[int, int]:
        """
        Get the coordinates of the object.

        Returns:
            tuple[int, int]: A tuple containing the x and y coordinates.
        """
        return (self.x, self.y)

    @coordinates.setter  # type: ignore
    def set_coordinates(self, coordinates: tuple[int, int]) -> None:
        """
        Set the coordinates of the object.

        Parameters:
            coordinates (tuple[int, int]): A tuple containing the x and y coordinates.
        """
        self.x, self.y = coordinates
