from collections import defaultdict


class UnionFind():

    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rank = [0]*(n+1)

    def find(self, x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        elif self.rank[x] > self.rank[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.root[self.find(x)]

    def roots(self):
        return [i for i, x in enumerate(self.root) if x < 0]

    def group_size(self):
        return len(self.roots())

    def group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members


def main():

    h, w = map(int, input().split())
    n = int(input())
    board = [[False] * w for _ in range(h)]
    uf = UnionFind(h*w)
    for _ in range(n):    
        ql = list(map(lambda x: int(x)-1, input().split()))
        if ql[0] == 0:
            board[ql[1]][ql[2]] = True
            if ql[1] > 0 and board[ql[1]-1][ql[2]]:
                uf.unite(ql[1]*w+ql[2], (ql[1]-1)*w+ql[2])
            if ql[1] < h - 1 and board[ql[1]+1][ql[2]]:
                uf.unite(ql[1]*w+ql[2], (ql[1]+1)*w+ql[2])
            if ql[2] < w - 1 and board[ql[1]][ql[2]+1]:
                uf.unite(ql[1]*w+ql[2], (ql[1])*w+ql[2]+1)
            if ql[2] > 0 and board[ql[1]][ql[2]-1]:
                uf.unite(ql[1]*w+ql[2], (ql[1])*w+ql[2]-1)
        else:
            print("Yes" if board[ql[1]][ql[2]] and board[ql[3]][ql[4]] and uf.same(ql[1]*w+ql[2], ql[3]*w+ql[4]) else "No")

if __name__ == '__main__':
    main()
