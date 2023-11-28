

import json

import pyperf
from Algorithms.jarvismarch import JarvisMarch
from Algorithms.quickhull import QuickHull

from point import Point

runner = pyperf.Runner()

with open('./Data/50_points_3_hull_points.json', 'r') as f:
        data = json.load(f)

points = list(map(lambda d: Point(d[0], d[1]) ,data))
runner.bench_func('50 Gaussian and 3 hull points - Jarvis March', JarvisMarch, points)
runner.bench_func('50 Gaussian and 3 hull points - Quickhull', QuickHull, points)

with open('./Data/50_points_4_hull_points.json', 'r') as f:
        data = json.load(f)

points = list(map(lambda d: Point(d[0], d[1]) ,data))
runner.bench_func('50 Gaussian and 4 hull points - Jarvis March', JarvisMarch, points)
runner.bench_func('50 Gaussian and 4 hull points - Quickhull', QuickHull, points)

with open('./Data/50_points_5_hull_points.json', 'r') as f:
        data = json.load(f)

points = list(map(lambda d: Point(d[0], d[1]) ,data))
runner.bench_func('50 Gaussian and 5 hull points - Jarvis March', JarvisMarch, points)
runner.bench_func('50 Gaussian and 5 hull points - Quickhull', QuickHull, points)

with open('./Data/100_points_3_hull_points.json', 'r') as f:
        data = json.load(f)

points = list(map(lambda d: Point(d[0], d[1]) ,data))
runner.bench_func('100 Gaussian and 3 hull points - Jarvis March', JarvisMarch, points)
runner.bench_func('100 Gaussian and 3 hull points - Quickhull', QuickHull, points)

with open('./Data/100_points_4_hull_points.json', 'r') as f:
        data = json.load(f)

points = list(map(lambda d: Point(d[0], d[1]) ,data))
runner.bench_func('100 Gaussian and 4 hull points - Jarvis March', JarvisMarch, points)
runner.bench_func('100 Gaussian and 4 hull points - Quickhull', QuickHull, points)

with open('./Data/100_points_5_hull_points.json', 'r') as f:
        data = json.load(f)

points = list(map(lambda d: Point(d[0], d[1]) ,data))
runner.bench_func('100 Gaussian and 5 hull points - Jarvis March', JarvisMarch, points)
runner.bench_func('100 Gaussian and 5 hull points - Quickhull', QuickHull, points)

with open('./Data/5000_points_3_hull_points.json', 'r') as f:
        data = json.load(f)

points = list(map(lambda d: Point(d[0], d[1]) ,data))
runner.bench_func('5000 Gaussian and 3 hull points - Jarvis March', JarvisMarch, points)
runner.bench_func('5000 Gaussian and 3 hull points - Quickhull', QuickHull, points)

with open('./Data/5000_points_4_hull_points.json', 'r') as f:
        data = json.load(f)

points = list(map(lambda d: Point(d[0], d[1]) ,data))
runner.bench_func('5000 Gaussian and 4 hull points - Jarvis March', JarvisMarch, points)
runner.bench_func('5000 Gaussian and 4 hull points - Quickhull', QuickHull, points)

with open('./Data/5000_points_5_hull_points.json', 'r') as f:
        data = json.load(f)

points = list(map(lambda d: Point(d[0], d[1]) ,data))
runner.bench_func('5000 Gaussian and 5 hull points - Jarvis March', JarvisMarch, points)
runner.bench_func('5000 Gaussian and 5 hull points - Quickhull', QuickHull, points)

with open('./Data/50000_points_3_hull_points.json', 'r') as f:
        data = json.load(f)

points = list(map(lambda d: Point(d[0], d[1]) ,data))
runner.bench_func('50000 Gaussian and 3 hull points - Jarvis March', JarvisMarch, points)
runner.bench_func('50000 Gaussian and 3 hull points - Quickhull', QuickHull, points)

with open('./Data/50000_points_4_hull_points.json', 'r') as f:
        data = json.load(f)

points = list(map(lambda d: Point(d[0], d[1]) ,data))
runner.bench_func('50000 Gaussian and 4 hull points - Jarvis March', JarvisMarch, points)
runner.bench_func('50000 Gaussian and 4 hull points - Quickhull', QuickHull, points)

with open('./Data/50000_points_5_hull_points.json', 'r') as f:
        data = json.load(f)

points = list(map(lambda d: Point(d[0], d[1]) ,data))
runner.bench_func('50000 Gaussian and 5 hull points - Jarvis March', JarvisMarch, points)
runner.bench_func('50000 Gaussian and 5 hull points - Quickhull', QuickHull, points)