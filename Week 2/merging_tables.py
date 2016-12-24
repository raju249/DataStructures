# python3

import sys
    
class DisJointSet():
    def __init__(self, n, lines):
        self.n  = n
        self.lines = [0] + lines
        self.rank = [0] * (n + 1)
        self.parent = list(range(0, n + 1))
        self.max = max(self.lines)

    # Find the parent and perform path compression
    def get_parent(self, i):
        root = i

        parent_to_update = []

        while root != self.parent[root]:
            parent_to_update.append(self.parent[root])
            root = self.parent[root]

        for parent in parent_to_update:
            self.parent[parent] = root

        return root

    def merge(self, src, dest):
        _src = self.get_parent(src)
        _dest = self.get_parent(dest)

        if _src == _dest:
            return

        if self.rank[_src] >= self.rank[_dest]:
            self.parent[_src] = _dest
        else:
            self.parent[_dest] = _src
            if self.rank[_src] == self.rank[_dest]:
                self.rank[_src] = self.rank[_src] + 1

        self.lines[_dest] += self.lines[_src]
        self.lines[_src] = 0

        if self.lines[_dest] > self.max:
            self.max = self.lines[_dest]

    def get_max(self):
        print(self.max)

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    lines = list(map(int, sys.stdin.readline().split()))
    dSet = DisJointSet(n, lines)
    for i in range(m):
        destination, source = map(int, sys.stdin.readline().split())
        dSet.merge(source, destination)
        dSet.get_max()