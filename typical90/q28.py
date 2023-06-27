# 2次元いもす法

def main():

    n = int(input())
    lrxy = [map(int, input().split()) for _ in range(n)]
    tiles = [[0] * 1002 for _ in range(1002)]
    for lx, ly, rx, ry in lrxy:
        tiles[lx][ly] += 1
        tiles[rx][ry] += 1
        tiles[lx][ry] -= 1
        tiles[rx][ly] -= 1
    for i in range(1001):
        for j in range(1001):
            tiles[i][j+1] += tiles[i][j]
    for i in range(1001):
        for j in range(1001):
            tiles[i+1][j] += tiles[i][j]
    ans = [0] * (n+1)
    for i in range(1002):
        for j in range(1002):
            ans[tiles[i][j]] += 1
    for i in range(1, n+1):
        print(ans[i])

if __name__ == '__main__':
    main()

"""

"""