import pyperf
import time
import json
from Algorithms.jarvismarch import JarvisMarch
from Algorithms.quickhull import QuickHull
from point import Point

runner = pyperf.Runner()

with open('./Data/10_gaussian_points.json', 'r') as f:
    data = json.load(f)

points = list(map(lambda d: Point(d[0], d[1]) ,data))
runner.bench_func('10 Gaussian points - Jarvis March', JarvisMarch, points)
runner.bench_func('10 Gaussian points - Quickhull', QuickHull, points)

with open('./Data/50_gaussian_points.json', 'r') as f:
    data = json.load(f)

points = list(map(lambda d: Point(d[0], d[1]) ,data))
runner.bench_func('50 Gaussian points - Jarvis March', JarvisMarch, points)
runner.bench_func('50 Gaussian points - Quickhull', QuickHull, points)

with open('./Data/100_gaussian_points.json', 'r') as f:
    data = json.load(f)

points = list(map(lambda d: Point(d[0], d[1]) ,data))
runner.bench_func('100 Gaussian points - Jarvis March', JarvisMarch, points)
runner.bench_func('100 Gaussian points - Quickhull', QuickHull, points)

with open('./Data/500_gaussian_points.json', 'r') as f:
    data = json.load(f)

points = list(map(lambda d: Point(d[0], d[1]) ,data))
runner.bench_func('500 Gaussian points - Jarvis March', JarvisMarch, points)
runner.bench_func('500 Gaussian points - Quickhull', QuickHull, points)

with open('./Data/1000_gaussian_points.json', 'r') as f:
    data = json.load(f)

points = list(map(lambda d: Point(d[0], d[1]) ,data ))
runner.bench_func('1000 Gaussian points - Jarvis March', JarvisMarch, points)
runner.bench_func('1000 Gaussian points - Quickhull', QuickHull, points)

with open('./Data/5000_gaussian_points.json', 'r') as f:
    data = json.load(f)

points = list(map(lambda d: Point(d[0], d[1]) ,data ))
runner.bench_func('5000 Gaussian points - Jarvis March', JarvisMarch, points)
runner.bench_func('5000 Gaussian points - Quickhull', QuickHull, points)

with open('./Data/10000_gaussian_points.json', 'r') as f:
    data = json.load(f)

points = list(map(lambda d: Point(d[0], d[1]) ,data))
runner.bench_func('10000 Gaussian points - Jarvis March', JarvisMarch, points)
runner.bench_func('10000 Gaussian points - Quickhull', QuickHull, points)

with open('./Data/50000_gaussian_points.json', 'r') as f:
    data = json.load(f)

points = list(map(lambda d: Point(d[0], d[1]) ,data))
runner.bench_func('50000 Gaussian points - Jarvis March', JarvisMarch, points)
runner.bench_func('50000 Gaussian points - Quickhull', QuickHull, points)