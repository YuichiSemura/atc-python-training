def main():

    n = int(input())
    al = [map(int, input().split()) for _ in range(n)]
    dp = [[0] * 2 for _ in range(n+1)]
    dp[0][0] = 0
    dp[0][1] = 0
    for ind, (x, y) in enumerate(al):
        if x == 0:
            dp[ind+1][0] = max([dp[ind][0], dp[ind][0] + y, dp[ind][1] + y])
            dp[ind+1][1] = dp[ind][1]
        else:
            dp[ind+1][0] = dp[ind][0]
            dp[ind+1][1] = max(dp[ind][0] + y, dp[ind][1])
    print(max(dp[n]))

if __name__ == '__main__':
    main()

"""

"""