from copy import copy
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

# Confirm that when there are colinear points and we encounter the furthest point first we keep that point for the convex hull.
def test_colinear_points_with_further_point_first():
    points = [Point(1,2), Point(3,6), Point(2, 4), Point(4,1)]

    # QuickHull starts by sorting the points and as a result it changes the variable here. I use copy to avoid changing the order of points
    # in this function, so I can use my hack for making sure the QuickHull results are correct.
    hull = QuickHull(copy(points))

    answer = [points[0], points[1], points[3]]
    assert all(p in hull for p in answer)

# Confirm that when there are colinear points and we encounter the closer point first we switch to the further point for the convex hull.
def test_colinear_points_with_closer_point_first():
    points = [Point(1,2), Point(2, 4), Point(3,6), Point(4,1)]
    hull = QuickHull(points)

    answer = [points[0], points[2], points[3]]
    assert all(p in hull for p in answer)

def test_only_colinear_points():
    points = [Point(1,2), Point(2, 4), Point(3,6)]
    hull = QuickHull(points)

    answer = [points[0], points[2]]
    assert all(p in hull for p in answer)

# Confirm that the algorithm works when points are positive or negative
def test_negative_and_positive_points_all_are_hull_points():
    points = [Point(1,2), Point(2, -4), Point(-3,-6)]
    hull = QuickHull(points)

    assert all(p in hull for p in points)