from Algorithms import quickhull, jarvismarch
from point import Point
import numpy as np
import matplotlib.pyplot as plt
import scipy

if __name__ == '__main__':
    rng = np.random.default_rng()
    data_points_gauss = (25*rng.random(size=(50,2))).round().astype(int)

    print("Would you like to use Quickhull or Jarvis March? (Q=Quickhull, J=Jarvis March)")
    alg = input()

    uniquePoints: set = set()
    for p in data_points_gauss.tolist():
        uniquePoints.add((p[0], p[1]))

    points = list(map(lambda up: Point(up[0], up[1]), uniquePoints))
    if (alg.lower() == 'q'):
        hull = quickhull.QuickHull(points)
    elif (alg.lower() == 'j'):
        hull = jarvismarch.JarvisMarch(points)

    pointsNotInHull = list(set(points) - hull)
    fig, ax = plt.subplots()
    ax.scatter(list(map(lambda p: p.x, pointsNotInHull)), 
               list(map(lambda p: p.y, pointsNotInHull)), label='Interior Points')
    ax.scatter(list(map(lambda p: p.x, hull)), 
               list(map(lambda p: p.y, hull)), label='Hull Points')
    
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=fig.transFigure)
    plt.show()