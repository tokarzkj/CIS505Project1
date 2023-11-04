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

    answer = [points[0], points[1], points[2]]
    assert all(p in hull for p in answer)

def test_some_points_are_hull_points():
    points = [Point(1, 2), Point(3, 3), Point(5, 6), Point(6, 1)]
    hull = QuickHull(points)

    answer = [points[0], points[2], points[3]]
    assert all(p in hull for p in answer)