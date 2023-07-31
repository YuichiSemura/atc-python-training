def main():

    mod = 998244353
    n = int(input())
    al = [0] + list(map(int, input().split()))
    mask = 2047
    # 10 になれば他の状態は関係ないので 1025
    ll = 1025
    dp = [[0] * ll for _ in range(n+1)]
    dp[0][1] = 1
    for i in range(1, n + 1):
        p = pow(al[i], mod - 2, mod)
        for j in range(ll):
            for x in range(1, min(10, al[i]) + 1):
                s = min((j | (j << x)) & mask, 1024)
                dp[i][s] = (dp[i][s] + dp[i-1][j] * p) % mod
            if al[i] > 10:
                dp[i][j] = (dp[i][j] + dp[i-1][j] * p % mod * (al[i] - 10)) % mod
    print(dp[-1][-1])

if __name__ == '__main__':
    main()

"""

"""