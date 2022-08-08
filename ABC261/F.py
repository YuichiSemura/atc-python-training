class Fenwick_Tree:
    def __init__(self, n):
        self._n = n
        self.data = [0] * n

    def add(self, p, x):
        assert 0 <= p < self._n
        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def sum(self, l, r):
        assert 0 <= l <= r <= self._n
        return self._sum(r) - self._sum(l)

    def _sum(self, r):
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r
        return s

def main():

    n = int(input())
    cl = list(map(int, input().split()))
    xl = list(map(int, input().split()))
    
    c_list = [[] for _ in range(n+1)]
    for c, x in zip(cl, xl):
        c_list[c].append(x)

    count = 0
    fw = Fenwick_Tree(n+1)
    for x in xl:
        fw.add(n-x, 1)
        count += fw.sum(0, n-x)

    for x in xl:
        fw.add(n-x, -1)
    
    for cxl in c_list:
        for x in cxl:
            fw.add(n-x, 1)
            count -= fw.sum(0, n-x)
        
        for x in cxl:
            fw.add(n-x, -1)
        
    print(count)

if __name__ == '__main__':
    main()

