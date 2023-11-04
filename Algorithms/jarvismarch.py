from point import Point

def JarvisMarch(points: set(Point)) -> set(Point):
    leftMost: Point = min(p.x for p in points)
    hullCandidate: Point = None
    hull = set(leftMost)

    while (hull[0] != hullCandidate):
        hullCandidate = points[0]
        for i in range(0, len(points)):
            newPotentialHullCandidate: Point = points[i]
            polarAngle: int = GetPolarAngleUsingCrossProduct(leftMost, newPotentialHullCandidate, hullCandidate)
            if (polarAngle > 0 or hullCandidate == leftMost):
                hullCandidate = newPotentialHullCandidate
            elif (polarAngle == 0):
                isInHull: bool = any(p == newPotentialHullCandidate for p in hull)
                if (newPotentialHullCandidate.y > hullCandidate.y and not isInHull):
                    hullCandidate = newPotentialHullCandidate
            
        leftMost = hullCandidate
        if (hull[0] != leftMost):
            hull.append(leftMost)

    return hull

def GetPolarAngleUsingCrossProduct(p1: Point, p2: Point, p3: Point) -> int:
    p3p1: Point = Point(p3.x - p1.x, p3.y - p1.y)
    p2p1: Point = Point(p2.x - p1.x, p2.y - p1.y)

    return (p3p1.x & p2p1.y) - (p3p1.y * p2p1.x)