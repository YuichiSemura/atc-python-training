class SegTree:
    def __init__(self, op, e, n, v=None):
        self._n = n
        self._op = op
        self._e = e
        self._log = (n - 1).bit_length()
        self._size = 1 << self._log
        self._d = [self._e()] * (self._size << 1)
        if v is not None:
            for i in range(self._n):
                self._d[self._size + i] = v[i]
            for i in range(self._size - 1, 0, -1):
                self._d[i] = self._op(self._d[i << 1], self._d[i << 1 | 1])

    def set(self, p, x):
        p += self._size
        self._d[p] = x
        while p:
            self._d[p >> 1] = self._op(self._d[p], self._d[p ^ 1])
            p >>= 1

    def get(self, p):
        return self._d[p + self._size]

    def prod(self, l, r):
        sml, smr = self._e(), self._e()
        l += self._size
        r += self._size
        while l < r:
            if l & 1:
                sml = self._op(sml, self._d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self._op(self._d[r], smr)
            l >>= 1
            r >>= 1
        return self._op(sml, smr)

    def all_prod(self):
        return self._d[1]

def op(x, y):
    return max(x, y)

def e():
    return - 10 ** 16

def main():

    w, n = map(int, input().split())
    lrvl = [map(int, input().split()) for _ in range(n)]
    
    dp = [0] + [- 10 ** 16] * (w)
    for i, (l, r, v) in enumerate(lrvl):
        seg = SegTree(op, e, w+1, dp)
        dp = [dd for dd in dp]
        for j in range(1, w+1):
            if j-l >= 0:
                # print(j, max(0, j-r), j-l, seg.get(max(0, j-r)), seg.prod(max(0, j-r), j-l+1) + v)
                dp[j] = max(seg.get(j), seg.prod(max(0, j-r), j-l+1) + v)
        # print(dp)
    print(dp[w] if dp[w] > 0 else -1)


if __name__ == '__main__':
    main()

"""
100 4
30 40 120
30 40 30
30 40 1500
30 40 40

100 4
13 15 31415
12 13 92653
29 33 58979
95 98 32384

5000 5
1000 1000 1000000000
1000 1000 1000000000
1000 1000 1000000000
1000 1000 1000000000
1000 1000 1000000000

100 5
20 20 1000
20 20 1000
20 20 1000
20 20 1000
20 20 1000

"""