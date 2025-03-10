import os, sys
from functools import cmp_to_key

try:
    from compile_with_soln import grader_stub
    grader = grader_stub()
except:
    pass

N = 0
D = 0
K = 0

def get_class_local(index):
    if index < 0 or index >= 8:
        print('get_class_local: Invalid point index!')
        sys.exit(0)
    return 1 if index < 4 else -1

def get_coord_local(i, j):
    pts = [[0.0, 0.0], [4.0, 0.0], [4.0, 3.0], [0.0, 3.0],
           [3.0, 1.0], [8.0, 1.0], [8.0, 4.0], [3.0, 4.0]]
    if i < 0 or i >= 8:
        print('get_coord_local: Invalid point index!')
        sys.exit(0)
    if j < 0 or j >= 2:
        print('get_coord_local: Invalid coordinate index!')
        sys.exit(0)
    return pts[i][j]

def getClass(index):
    if 'grader' in globals() and hasattr(grader, 'get_class'):
        return grader.get_class(index)
    return get_class_local(index)

def getCoord(i, j):
    if 'grader' in globals() and hasattr(grader, 'get_coord'):
        return grader.get_coord(i, j)
    return get_coord_local(i, j)

def distanceSquared(a, b):
    s = 0
    for i in range(len(a)):
        diff = a[i] - b[i]
        s += diff * diff
    return s

class KdNode:
    def __init__(self, pointIndex, axis, left, right):
        self.pointIndex = pointIndex
        self.axis = axis
        self.left = left
        self.right = right

def buildKdTree(indices, depth, pointsList):
    if not indices:
        return None
    axis = depth % len(pointsList[0])
    indices.sort(key=lambda i: pointsList[i][axis])
    mid = len(indices) // 2
    return KdNode(indices[mid], axis, buildKdTree(indices[:mid], depth+1, pointsList), buildKdTree(indices[mid+1:], depth+1, pointsList))

def searchKdTree(node, query, k, excludeIndex, pointsList, neighbors):
    if node is None:
        return
    idx = node.pointIndex
    if idx != excludeIndex:
        d = distanceSquared(query, pointsList[idx])
        if len(neighbors) < k:
            neighbors.append((d, idx))
        else:
            maxD = max(neighbors, key=lambda x: x[0])[0]
            if d < maxD:
                for j in range(len(neighbors)):
                    if neighbors[j][0] == maxD:
                        neighbors[j] = (d, idx)
                        break
    axis = node.axis
    diff = query[axis] - pointsList[node.pointIndex][axis]
    if diff <= 0:
        near = node.left
        far = node.right
    else:
        near = node.right
        far = node.left
    searchKdTree(near, query, k, excludeIndex, pointsList, neighbors)
    if len(neighbors) < k or diff * diff < max(neighbors, key=lambda x: x[0])[0]:
        searchKdTree(far, query, k, excludeIndex, pointsList, neighbors)

def main():
    global N, D, K
    try:
        N = int(os.environ["N"])
        D = int(os.environ["D"])
        K = int(os.environ["K"])
    except:
        N = 8
        D = 2
        K = 3
    points = []
    for i in range(N):
        pt = []
        for j in range(D):
            pt.append(getCoord(i, j))
        points.append(pt)
    kdTree = buildKdTree(list(range(N)), 0, points)
    confMatrix = [[0, 0], [0, 0]]
    for i in range(N):
        query = points[i]
        neighbors = []
        searchKdTree(kdTree, query, K, i, points, neighbors)
        vote = 0
        for d, idx in neighbors:
            vote += getClass(idx)
        pred = 1 if vote > 0 else -1
        actual = getClass(i)
        if actual == 1:
            if pred == 1:
                confMatrix[0][0] += 1
            else:
                confMatrix[0][1] += 1
        else:
            if pred == 1:
                confMatrix[1][0] += 1
            else:
                confMatrix[1][1] += 1
    print(f"{confMatrix[0][0]} {confMatrix[0][1]}")
    print(f"{confMatrix[1][0]} {confMatrix[1][1]}")

if __name__ == "__main__":
    main()
