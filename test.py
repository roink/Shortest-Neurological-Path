from brain_path import BrainPath
from paths import Paths
from kpaths import KPaths
from copy import deepcopy
from heapq import heappush
from heapq import heappop


p = BrainPath(5)


k = 10
ps = Paths(k,20)

print(p)

for i in range(20):
    p = p.add(i,1)
    print(p)
    print(ps.add(p))
    print(ps.add(p))

p = BrainPath(1)
for i in range(20):
    p = p.add(i,0.1)
    print(p)
    print(ps.add(p))
    print(ps.add(p))
    print(len(ps))


print(ps)
print(len(ps))