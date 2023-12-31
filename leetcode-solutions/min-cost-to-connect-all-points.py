class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]

    def unionFind(self, a):
        if a != self.parent[a]:
            self.parent[a] = self.unionFind(self.parent[a])
        return self.parent[a]
    
    def union(self, a, b):
        a = self.unionFind(a)
        b = self.unionFind(b)
        if b < a:
            a,b = b,a
        self.parent[b] = a
        
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        edges = []
        length = len(points)
        for i in range(length):
            for j in range(i+1,length):
                distance = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                edges.append((distance,i,j))

        Union = UnionFind(length)
        total = 0   
        edges.sort()
        for distance,a,b in edges:
            if Union.unionFind(a) != Union.unionFind(b):
                total += distance
                Union.union(a,b)

        return total




