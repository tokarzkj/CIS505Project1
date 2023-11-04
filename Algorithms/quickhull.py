from point import Point
import math

def QuickHull(points: list) -> list:
    if (points is None or len(points) < 3):
        raise ValueError("points parameter must have 3 or more points") 
    
    points.sort(key= lambda p: p.x)
    leftMost: Point = points[0]
    rightMost: Point = points[-1]
    hull = set([leftMost, rightMost])  

    leftPoints = []
    rightPoints = []

    for i in range(0, len(points)):
        polarAngle: int = GetPolarAngleUsingCrossProduct(leftMost, points[i], rightMost)
        if (points[i] in hull):
            continue

        # If polarAngle > 0, then this is a right turning segment and the middle point must be above the line.
        # If polarAngle < 0, then it is an implied left turn
        if polarAngle > 0:
            leftPoints.append(points[i])
        elif polarAngle < 0:
            rightPoints.append(points[i])

    leftHull: list = FindHullPoints(leftPoints, leftMost, rightMost)
    rightHull: list = FindHullPoints(rightPoints, rightMost, leftMost)

    if (leftHull is not None):
        hull.update(leftHull)

    if (rightHull is not None):
        hull.update(rightHull)

    return hull

def FindHullPoints(remainingPoints: list, left: Point, right: Point) -> list:
    if (len(remainingPoints) == 0):
        return
    
    lineSegment = Point(right.x - left.x, right.y - left.y)
    furthestPoint = (0, None)

    for i in range(0, len(remainingPoints)):
        distance: float = GetDistance(lineSegment, remainingPoints[i])
        if (distance > furthestPoint[0]):
            furthestPoint = (distance, remainingPoints[i])

    if (furthestPoint[1] is None):
        return

    leftPoints: list = []
    rightPoints: list = []

    for i in range(0, len(remainingPoints)):
        polarAngle: int = GetPolarAngleUsingCrossProduct(left, remainingPoints[i], right)
        if (remainingPoints[i] == left or remainingPoints[i] == right or remainingPoints[i] == furthestPoint[1]):
            continue

        # If polarAngle > 0, then this is a right turning segment and the middle point must be above the line.
        # If polarAngle < 0, then it is an implied left turn
        if polarAngle > 0:
            leftPoints.append(remainingPoints[i])
        elif polarAngle < 0:
            rightPoints.append(remainingPoints[i])

    leftHull = FindHullPoints(leftPoints, left, furthestPoint[1])
    rightHull = FindHullPoints(rightPoints, furthestPoint[1], right)

    result = [furthestPoint[1]]

    if (leftHull is not None):
        result.extend(leftHull)
    
    if (rightHull is not None):
        result.extend(rightHull)

    return result


def GetPolarAngleUsingCrossProduct(p1: Point, p2: Point, p3: Point) -> int:
    p3p1: Point = Point(p3.x - p1.x, p3.y - p1.y)
    p2p1: Point = Point(p2.x - p1.x, p2.y - p1.y)

    return (p3p1.x & p2p1.y) - (p3p1.y * p2p1.x)

def GetDistance(lineSegment, point) -> float:
    return abs(
        (lineSegment.x * point.y) - (lineSegment.y * point.x)
    )