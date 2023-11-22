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

# Confirm that if we encounter data sets with the same x value, but different y values works
def test_multiple_x_values_with_different_y_values():
    points = [Point(1,2), Point(1, -4), Point(-3,-6)]
    hull = QuickHull(points)

    assert all(p in hull for p in points)

def test_with_points_in_all_quadrants():
    points = [Point(-5, -5), Point(-31, 36), Point(-18, 37), Point(8, 1), Point(-16, -3), Point(-14, 24),
              Point(-11, 6), Point(-5, 15), Point(26, 30), Point(11, -14), Point(23, -30)]
    hull = QuickHull(copy(points))

    answer = [points[1], points[2], points[8], points[10], points[4]]
    assert all(p in hull for p in answer)

def test_points_close_to_hull():
    points = [Point(-2.415507919565558, -0.5242918153835444), Point(1.6550678142353963, 1.2095408862776673), 
              Point(0.18672128724192494, 1.9090457502641769), Point(-1.1357405014212403, 0.39298901707602199),
              Point(2.6719628088750174, -0.4666324100015172)]
    
    hull = QuickHull(copy(points))
    answer = [points[0], points[2], points[1], points[4]]
    assert all(p in hull for p in answer)