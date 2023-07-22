def main():

    h, w, n = map(int, input().split())
    abl = [map(int, input().split()) for _ in range(n)]
    g = [[False] * w for _ in range(h)]
    for a, b in abl:
        g[a-1][b-1] = True
    dp = [[0] * w for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if g[i][j]:
                continue
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            ans += dp[i][j]
    print(ans)

if __name__ == '__main__':
    main()

"""

"""