def main():

    n = int(input())
    al = list(map(int, input().split()))
    count = 0
    for i in range(1, n+1):
        dp = [[[0] * i for _ in range(i+1)] for _ in range(n+1)]
        dp[0][0][0] = 1
        for j in range(n):
            for k in range(i+1):
                for l in range(i):
                    dp[j+1][k][l] += dp[j][k][l]
                    dp[j+1][k][l] %= 998244353
                    if k != i:
                        dp[j+1][k+1][(l+al[j])%i] += dp[j][k][l]
                        dp[j+1][k+1][(l+al[j])%i] %= 998244353
        count += dp[-1][i][0]
        count %= 998244353
    print(count)


if __name__ == '__main__':
    main()
