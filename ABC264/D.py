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

    s = input()
    
    def replace_atcoder(ch):
        if ch == "a":
            return 1
        if ch == "t":
            return 2
        if ch == "c":
            return 3
        if ch == "o":
            return 4
        if ch == "d":
            return 5
        if ch == "e":
            return 6
        if ch == "r":
            return 7
        
    numl = [replace_atcoder(ch) for ch in s]
    count = 0
    n = 8
    fw = Fenwick_Tree(n)
    for x in numl:
        fw.add(n-x, 1)
        count += fw.sum(0, n-x)
    print(count)

if __name__ == '__main__':
    main()