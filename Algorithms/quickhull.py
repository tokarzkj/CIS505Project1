from point import Point

def QuickHull(points: list) -> list:
    if (points is None or len(points) < 3):
        raise ValueError("points parameter must have 3 or more points") 
    
    points.sort(key= lambda p: p.x)
    leftMost: Point = points[0]
    rightMost: Point = points[-1]
 
    leftPoints = []
    rightPoints = []

    for i in range(0, len(points)):
        polarAngle: int = GetPolarAngleUsingCrossProduct(leftMost, points[i], rightMost)
        if (points[i] == leftMost or points[i] == rightMost):
            continue

        # If polarAngle > 0, then this is a right turning segment and the middle point must be above the line.
        # If polarAngle < 0, then it is an implied left turn
        if polarAngle > 0:
            leftPoints.append(points[i])
        elif polarAngle < 0:
            rightPoints.append(points[i])

    leftHull: list = FindHullPoints(leftPoints, leftMost, rightMost)
    rightHull: list = FindHullPoints(rightPoints, rightMost, leftMost)

    hull = [leftMost] 
    if (leftHull is not None):
        hull.extend(leftHull)

    hull.append(rightMost)

    if (rightHull is not None):
        hull.extend(rightHull)


    return hull

def FindHullPoints(remainingPoints: list, left: Point, right: Point) -> list:
    if (remainingPoints is None or len(remainingPoints) == 0):
        return

    furthestPoint = (0, None)

    for i in range(0, len(remainingPoints)):
        distance: float = GetPointsDistanceFromLine(left, remainingPoints[i], right)
        if (distance > furthestPoint[0]):
            furthestPoint = (distance, remainingPoints[i])

    leftPoints: list = []
    rightPoints: list = []

    for i in range(0, len(remainingPoints)):
        if (remainingPoints[i] == left or remainingPoints[i] == right or remainingPoints[i] == furthestPoint[1]):
            continue

        leftSidePolarAngle: int = GetPolarAngleUsingCrossProduct(left, remainingPoints[i], furthestPoint[1])
        rightSidePolarAngle: int = GetPolarAngleUsingCrossProduct(right, remainingPoints[i], furthestPoint[1])

        # If polarAngle > 0, then this is a right turning segment and the middle point must be above the line.
        # If polarAngle < 0, then it is an implied left turn
        if leftSidePolarAngle > 0:
            leftPoints.append(remainingPoints[i])
        elif rightSidePolarAngle < 0:
            rightPoints.append(remainingPoints[i])

    leftHull = FindHullPoints(leftPoints, left, furthestPoint[1])
    rightHull = FindHullPoints(rightPoints, furthestPoint[1], right)

    result = []

    if (leftHull is not None):
        result.extend(leftHull)
    
    result.append(furthestPoint[1])

    if (rightHull is not None):
        result.extend(rightHull)

    return result

def GetPolarAngleUsingCrossProduct(p1: Point, p2: Point, p3: Point) -> int:
    p3p1: Point = Point(p3.x - p1.x, p3.y - p1.y)
    p2p1: Point = Point(p2.x - p1.x, p2.y - p1.y)

    return (p3p1.x * p2p1.y) - (p3p1.y * p2p1.x)

# Using the following formula https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line#Line_defined_by_two_points.
# However, because the line segment is the same for all the points we are checking we can ignore the denominator since
# it will be the same, so the larger numerator is what we care about and we are working with whole numbers, so there is
# no division of less than 1.
def GetPointsDistanceFromLine(p1: Point, p2: Point, p3: Point) -> int:
    """Calculate a relative distance of p2 from the line segment made by p1 and p3"""
    return abs((p1.y - p2.y)*(p3.x - p1.x) - (p3.y - p1.y)*(p1.x - p2.x))
