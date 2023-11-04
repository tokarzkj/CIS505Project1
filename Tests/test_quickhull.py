import pytest
from Algorithms.quickhull import QuickHull
from point import Point

# Confirm we raise an error if none is passed in.
def test_none_points():
    with pytest.raises(ValueError):
        QuickHull(None)

# Confirm we raise an error when there are less than 3 points.
def test_less_than_3_points():
    with pytest.raises(ValueError):
        QuickHull([Point(1, 2), Point(3, 6)])

# Confirm that we can handle scenarios where all points are hull points.
def test_all_points_are_hull_points():
    points = [Point(1, 2), Point(3, 6), Point(4, 1)]
    hull = QuickHull(points)

    assert len(points), 3
    assert points == hull