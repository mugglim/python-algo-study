import sys
input = sys.stdin.readline

class DS:
    def __init__(self, n):
        self.parent = [x for x in range(n + 1)]

    def find(self, x):
        if self.parent[x] == x: return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX < rootY: self.parent[rootY] = rootX
        else: self.parent[rootX] = rootY

def main():
    n = int(input())
    m = int(input())

    graph = [list(map(int,input().split())) for _ in range(n)]
    trace = list(map(int,input().split()))


    ds = DS(n)

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1: ds.union(i + 1,j + 1)

    parent = ds.parent
    parentKinds = [parent[x] for x in trace]

    return len(set(parentKinds)) == 1

if __name__ == "__main__":
    ans = main()
    print("YES" if ans else "NO")


