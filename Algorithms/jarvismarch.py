from point import Point

def JarvisMarch(points: list) -> list:
    if (points is None or len(points) < 3):
        raise ValueError("points parameter must have 3 or more points") 

    firstPoint =  min(points, key=lambda p: p.x)
    leftMost: Point = firstPoint
    hullCandidate: Point = None
    hull = set([leftMost])
    orderedHull = [leftMost]

    while (firstPoint != hullCandidate):
        hullCandidate = points[0]
        for i in range(0, len(points)):
            newPotentialHullCandidate: Point = points[i]
            polarAngle: int = GetPolarAngleUsingCrossProduct(leftMost, newPotentialHullCandidate, hullCandidate)
            if (polarAngle > 0 or hullCandidate == leftMost):
                hullCandidate = newPotentialHullCandidate
            elif (polarAngle == 0):
                isInHull: bool = newPotentialHullCandidate in hull
                if (newPotentialHullCandidate.y > hullCandidate.y and not isInHull):
                    hullCandidate = newPotentialHullCandidate
            
        leftMost = hullCandidate
        if (firstPoint != leftMost):
            hull.add(leftMost)
            orderedHull.append(leftMost)

    return orderedHull

def GetPolarAngleUsingCrossProduct(p1: Point, p2: Point, p3: Point) -> int:
    p3p1: Point = Point(p3.x - p1.x, p3.y - p1.y)
    p2p1: Point = Point(p2.x - p1.x, p2.y - p1.y)

    return (p3p1.x * p2p1.y) - (p3p1.y * p2p1.x)