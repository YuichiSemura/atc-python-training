def main():

    n = int(input())
    dp = [[1] + [0] * (n-1) for _ in range(n)]
    for i in range(1, n):
        for j in range(1, i+1):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    for l in dp:
        print(" ".join([str(d) for d in l if d != 0]))
            
if __name__ == '__main__':
    main()