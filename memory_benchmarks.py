import numpy as np

from Algorithms.quickhull import QuickHull
from Algorithms.jarvismarch import JarvisMarch
from point import Point
import tracemalloc


print("############################################################")
print("Memory Usage, 100k points")
print("############################################################\n")
pointCount = 100000
rng = np.random.default_rng()
points = rng.standard_normal(size= (pointCount, 2), dtype=np.float_)
points = list(map(lambda d: Point(d[0], d[1]) , points))

tracemalloc.start()
JarvisMarch(points)
snapshot = tracemalloc.take_snapshot()
stats = snapshot.statistics('lineno')
print("Jarvis March Usage")
for stat in stats:
    print(stat)
print(tracemalloc.get_traced_memory())
tracemalloc.stop()

tracemalloc.clear_traces()
tracemalloc.reset_peak()

tracemalloc.start()
QuickHull(points)
snapshot = tracemalloc.take_snapshot()
stats = snapshot.statistics('lineno')
print("Quickhull Usage")
for stat in stats:
    print(stat)
print(tracemalloc.get_traced_memory())
tracemalloc.stop()

tracemalloc.clear_traces()
tracemalloc.reset_peak()

print("############################################################")
print("Memory Usage, 200k points")
print("############################################################\n")

pointCount = 200000
points = rng.standard_normal(size= (pointCount, 2), dtype=np.float_)
points = list(map(lambda d: Point(d[0], d[1]) , points))

tracemalloc.start()
JarvisMarch(points)
snapshot = tracemalloc.take_snapshot()
stats = snapshot.statistics('lineno')
print("Jarvis March Usage")
for stat in stats:
    print(stat)
print(tracemalloc.get_traced_memory())
tracemalloc.stop()

tracemalloc.clear_traces()
tracemalloc.reset_peak()

tracemalloc.start()
QuickHull(points)
snapshot = tracemalloc.take_snapshot()
stats = snapshot.statistics('lineno')
print("Quickhull Usage")
for stat in stats:
    print(stat)
print(tracemalloc.get_traced_memory())
tracemalloc.stop()

tracemalloc.clear_traces()
tracemalloc.reset_peak()

print("############################################################")
print("Memory Usage, 300k points")
print("############################################################\n")

pointCount = 300000
points = rng.standard_normal(size= (pointCount, 2), dtype=np.float_)
points = list(map(lambda d: Point(d[0], d[1]) , points))

tracemalloc.start()
JarvisMarch(points)
snapshot = tracemalloc.take_snapshot()
stats = snapshot.statistics('lineno')
print("Jarvis March Usage")
for stat in stats:
    print(stat)
print(tracemalloc.get_traced_memory())
tracemalloc.stop()

tracemalloc.clear_traces()
tracemalloc.reset_peak()

tracemalloc.start()
QuickHull(points)
snapshot = tracemalloc.take_snapshot()
stats = snapshot.statistics('lineno')
print("Quickhull Usage")
for stat in stats:
    print(stat)
print(tracemalloc.get_traced_memory())
tracemalloc.stop()

print("############################################################")
print("Memory Usage, 400k points")
print("############################################################\n")

pointCount = 400000
points = rng.standard_normal(size= (pointCount, 2), dtype=np.float_)
points = list(map(lambda d: Point(d[0], d[1]) , points))

tracemalloc.start()
JarvisMarch(points)
snapshot = tracemalloc.take_snapshot()
stats = snapshot.statistics('lineno')
print("Jarvis March Usage")
for stat in stats:
    print(stat)
print(tracemalloc.get_traced_memory())
tracemalloc.stop()

tracemalloc.clear_traces()
tracemalloc.reset_peak()

tracemalloc.start()
QuickHull(points)
snapshot = tracemalloc.take_snapshot()
stats = snapshot.statistics('lineno')
print("Quickhull Usage")
for stat in stats:
    print(stat)
print(tracemalloc.get_traced_memory())
tracemalloc.stop()