def main():

    n, m = map(int, input().split())
    xl = list(map(int, input().split()))
    ml = [0] * 5000
    for _ in range(m):
        c, y = map(int, input().split())
        ml[c-1] = y
    dp = [[0] + [-3 * 10 ** 12] * 5000 for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, 5001):
            dp[i][j] = dp[i-1][j-1] + xl[i-1] + ml[j-1]
        dp[i][0] = max(dp[i-1])
    print(max(dp[-1]))


if __name__ == '__main__':
    main()
