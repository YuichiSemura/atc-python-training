from math import gcd

# 要素数、初期値、単位元
class SparseTable:
    def calc(self, x, y): return gcd(x, y)

    def __init__(self, n, init_val, ide_ele):
        self.n = n
        k = n.bit_length()
        self.k = k
        self.ide_ele = ide_ele
        self.log_table = [[ide_ele] * n for _ in range(k + 1)]
        for i in range(n):
            self.log_table[0][i] = init_val[i]
        for i in range(k):
            d = 1 << i
            for j in range(n):
                if j + d >= n:
                    break
                self.log_table[i + 1][j] = self.calc(
                    self.log_table[i][j], self.log_table[i][j + d])

    def query(self, l, r):
        d = r - l
        if d <= 0:
            return self.ide_ele
        if d == 1:
            return self.log_table[0][l]
        m = d.bit_length() - 1
        return self.calc(self.log_table[m][l], self.log_table[m][r - (1 << m)])


def main():

    n, q = map(int, input().split())
    al = list(map(int, input().split()))
    bl = list(map(int, input().split()))
    adif = [al[0]] + [0] * (n-1)
    bdif = [bl[0]] + [0] * (n-1)
     
    for i in list(range(1, n)):
        adif[i] = al[i] - al[i-1]
        bdif[i] = bl[i] - bl[i-1]
    
    sta = SparseTable(n, adif, 0)
    stb = SparseTable(n, bdif, 0)
    
    for _ in list(range(q)):
        h1, h2, w1, w2 = map(int, input().split())
        h1-=1
        w1-=1
        print(gcd(gcd(al[h1] + bl[w1], sta.query(h1 + 1, h2)), stb.query(w1 + 1, w2)))
        
if __name__ == '__main__':
    main()
    
"""
3 5
3 5 2
8 1 3
1 2 2 3
1 3 1 3
1 1 1 1
2 2 2 2
3 3 1 1

2
1
11
6
10
"""