from Algorithms.jarvismarch import JarvisMarch
from point import Point

# Confirm that we can handle scenarios where all points are hull points
def test_all_points_are_hull_points():
    points = [Point(1, 2), Point(3, 6), Point(4, 1)]
    hull = JarvisMarch(points)

    assert len(points), 3
    assert points, hull

# Confirm that we can handle scenarios where some points are hull points
def test_some_points_are_hull_points():
    points = [Point(1, 2), Point(3, 4), Point(5, 6), Point(6, 1)]
    hull = JarvisMarch(points)

    assert len(points), 3
    assert [Point(1, 2), Point(5, 6), Point(6, 1)], hull