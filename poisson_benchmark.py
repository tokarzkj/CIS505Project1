import pyperf
import time
import json
from Algorithms.jarvismarch import JarvisMarch
from Algorithms.quickhull import QuickHull
from point import Point

runner = pyperf.Runner()

with open('./Data/50_poisson_points.json', 'r') as f:
    data = json.load(f)

points = list(map(lambda d: Point(d[0], d[1]) ,data))
runner.bench_func('50 Poisson points - Jarvis March', JarvisMarch, points)
runner.bench_func('50 Poisson points - Quickhull', QuickHull, points)

with open('./Data/100_poisson_points.json', 'r') as f:
    data = json.load(f)

points = list(map(lambda d: Point(d[0], d[1]) ,data))
runner.bench_func('100 Poisson points - Jarvis March', JarvisMarch, points)
runner.bench_func('100 Poisson points - Quickhull', QuickHull, points)

with open('./Data/500_poisson_points.json', 'r') as f:
    data = json.load(f)

points = list(map(lambda d: Point(d[0], d[1]) ,data))
runner.bench_func('500 Poisson points - Jarvis March', JarvisMarch, points)
runner.bench_func('500 Poisson points - Quickhull', QuickHull, points)

with open('./Data/1000_poisson_points.json', 'r') as f:
    data = json.load(f)

points = list(map(lambda d: Point(d[0], d[1]) ,data ))
runner.bench_func('1000 Poisson points - Jarvis March', JarvisMarch, points)
runner.bench_func('1000 Poisson points - Quickhull', QuickHull, points)

with open('./Data/5000_poisson_points.json', 'r') as f:
    data = json.load(f)

points = list(map(lambda d: Point(d[0], d[1]) ,data ))
runner.bench_func('5000 Poisson points - Jarvis March', JarvisMarch, points)
runner.bench_func('5000 Poisson points - Quickhull', QuickHull, points)

with open('./Data/10000_poisson_points.json', 'r') as f:
    data = json.load(f)

points = list(map(lambda d: Point(d[0], d[1]) ,data ))
runner.bench_func('10000 Poisson points - Jarvis March', JarvisMarch, points)
runner.bench_func('10000 Poisson points - Quickhull', QuickHull, points)

#with open('./Data/50000_poisson_points.json', 'r') as f:
#    data = json.load(f)

#points = list(map(lambda d: Point(d[0], d[1]) ,data ))
#runner.bench_func('50000 Poisson points - Jarvis March', JarvisMarch, points)
#runner.bench_func('50000 Poisson points - Quickhull', QuickHull, points)