
from functools import reduce


def distance(p1, p2):
    return (abs(p1[0] - p2[0]) ** 2 + abs(p1[1] - p2[1]) ** 2 + abs(p1[2] - p2[2]) ** 2) ** 0.5


with open("08/input.txt") as f:
    points = [[int(num) for num in line.split(',')] for line in f.read().split('\n')]

edges = [(i, j) for i in range(len(points)) for j in range(i + 1, len(points))]
edges = sorted(edges, key=lambda edge: distance(points[edge[0]], points[edge[1]]))

parents = list(range(len(points)))
child_count = {i: 1 for i in range(len(points))}

def find_root(point):
    parent = parents[point]
    if parents[point] != point:
        root = find_root(parent)
        parents[point] = root
        return root
    return point

def merge_sets(point1, point2):
    r1, r2 = find_root(point1), find_root(point2)
    if r1 != r2:
        if child_count[r1] < child_count[r2]:
            parent, child = r2, r1
        else:
            parent, child = r1, r2
        parents[child] = parent
        child_count[parent] += child_count.pop(child)


for p1, p2 in edges:
    merge_sets(p1, p2)
    if len(child_count) <= 1:
        break

print(points[p1][0] * points[p2][0])
