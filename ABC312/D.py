def main():

    s = list(input())
    mod = 998244353
    ll = len(s) + 1
    dp = [[0] * ll for a in range(ll)]
    dp[0][0] = 1
    for i in range(1, ll):
        for j in range(ll):
            if s[i-1] == '?' or s[i-1] == '(':
                if j - 1 >= 0:
                    dp[i][j] = (dp[i][j] + dp[i-1][j-1]) % mod
            if s[i-1] == '?' or s[i-1] == ')':
                if j + 1 < ll:
                    dp[i][j] = (dp[i][j] + dp[i-1][j+1]) % mod
    print(dp[ll-1][0])
            

if __name__ == '__main__':
    main()

"""
(???(?

"""