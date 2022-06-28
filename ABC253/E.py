def main():

    n, m, k = map(int, input().split())
    mod = 998244353
    dp = [[0] * m for _ in range(n)]
    for j in range(m):
        dp[0][j] = 1
    for i in range(1, n):
        rl = []
        s = 0
        for j in range(m):
            s += dp[i-1][j]
            rl.append(s)
        for j in range(m):
            if j < k and m < j + k + 1:
                dp[i][j] = 0
            elif j < k:
                dp[i][j] = rl[-1] - rl[j+k-1]
            elif m < j + k + 1:
                dp[i][j] = rl[j-k]
            else:
                dp[i][j] = rl[-1] + rl[j-k] - rl[j+k-1]
            dp[i][j] %= mod
    print(sum(dp[-1]) % mod)

if __name__ == '__main__':
    main()
