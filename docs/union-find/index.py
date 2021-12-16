class DS:
    def __init__(self, n):
        self.parent = [x for x in range(n+1)]

    def find(self, x):
        if self.parent[x] == x: return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union( self, x,y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX > rootY: self.parent[rootX] = rootY
        else: self.parent[rootY] = rootX



n = 6
querys = [(1,2), (2,3), (3,4), (4,5), (5,6)]


ds = DS(n)

for query in querys:
    x,y = query
    ds.union(x,y)

print(ds.parent[1:])