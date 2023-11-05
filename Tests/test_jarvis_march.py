import pytest
from Algorithms.jarvismarch import JarvisMarch
from point import Point

# Confirm we raise an error if none is passed in.
def test_none_points():
    with pytest.raises(ValueError):
        JarvisMarch(None)

# Confirm we raise an error when there are less than 3 points.
def test_less_than_3_points():
    with pytest.raises(ValueError):
        JarvisMarch([Point(1, 2), Point(3, 6)])

# Confirm that we can handle scenarios where all points are hull points.
def test_all_points_are_hull_points():
    points = [Point(1, 2), Point(3, 6), Point(4, 1)]
    hull = JarvisMarch(points)

    assert len(points) == 3

    assert points == sorted(hull, key= lambda k: k.x)

# Confirm that we can handle scenarios where some points are hull points.
def test_some_points_are_hull_points():
    points = [Point(1, 2), Point(3, 3), Point(5, 6), Point(6, 1)]
    hull = JarvisMarch(points)

    answer = [points[0], points[2], points[3]]
    assert all(p in hull for p in answer)

# Confirm that when there are colinear points and we encounter the furthest point first we keep that point for the convex hull.
def test_colinear_points_with_further_point_first():
    points = [Point(1,2), Point(3,6), Point(2, 4), Point(4,1)]
    hull = JarvisMarch(points)

    answer = [points[0], points[1], points[3]]
    assert all(p in hull for p in answer)

# Confirm that when there are colinear points and we encounter the closer point first we switch to the further point for the convex hull.
def test_colinear_points_with_closer_point_first():
    points = [Point(1,2), Point(2, 4), Point(3,6), Point(4,1)]
    hull = JarvisMarch(points)

    answer = [points[0], points[2], points[3]]
    assert all(p in hull for p in answer)

# Confirm that when there are only colinear points we take the extremes for the convex hull.
def test_only_colinear_points():
    points = [Point(1,2), Point(2, 4), Point(3,6)]
    hull = JarvisMarch(points)

    answer = [points[0], points[2]]
    assert all(p in hull for p in answer)

# Confirm that the algorithm works when points are positive or negative
def test_negative_and_positive_points_all_are_hull_points():
    points = [Point(1,2), Point(2, -4), Point(-3,-6)]
    hull = JarvisMarch(points)

    assert all(p in hull for p in points)