def main():

    N = int(input())
    S = input()
    dp = [[0] * 7 for _ in list(range(N+1))]
    mod = 10 ** 9 + 7
    for ind, si in enumerate(S):
        for j in range(7):
            dp[ind+1][j] = dp[ind][j]
        if si == 'a':
            dp[ind+1][0] += 1
        elif si == 't':
            dp[ind+1][1] = dp[ind][1] + dp[ind][0]
        elif si == 'c':
            dp[ind+1][2] = dp[ind][2] + dp[ind][1]
        elif si == 'o':
            dp[ind+1][3] = dp[ind][3] + dp[ind][2]
        elif si == 'd':
            dp[ind+1][4] = dp[ind][4] + dp[ind][3]
        elif si == 'e':
            dp[ind+1][5] = dp[ind][5] + dp[ind][4]
        elif si == 'r':
            dp[ind+1][6] = dp[ind][6] + dp[ind][5]
        for j in range(7):
            dp[ind+1][j] = dp[ind+1][j] % mod
    # for d in dp:
    #     print(d)
    print(dp[-1][-1])

if __name__ == '__main__':
    main()
    
"""
4
4000 4400 5000 3200
3
3312
2992
4229

"""