# Simple hack file to generate test data.

import numpy as np
import json

rng = np.random.default_rng()

pointCount = 50000
points = rng.poisson(size=(pointCount, 2))

with open("./Data/{pointCount}_poisson_points.json".format(pointCount=pointCount), 'w') as f:
    json.dump(points.tolist(), f, indent=4)