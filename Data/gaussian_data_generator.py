# Simple hack file to generate test data.

import numpy as np
import json

rng = np.random.default_rng()
points = rng.standard_normal(size= (50, 2), dtype=np.float_)

with open('./Data/50_gaussian_points.json', 'w') as f:
    json.dump(points.tolist(), f, indent=4)