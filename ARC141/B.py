def main():

    mod = 998244353
    n, m = map(int, input().split())
    s = bin(m)
    ln = len(s)-2
    if ln < n:
        print(0)
        return
    x = 0
    if m != 1:
        x = (int(s[0:2]+s[3:], 2) + 1) % mod
    dp = [[0] * n for _ in range(ln)]
    for i in range(0, ln-1):
        dp[i][0] = pow(2, i+1, mod) - 1
    dp[-1][0] = m % mod
    for i in range(1, ln):
        for j in range(1, n):
            if i < j:
                continue
            d = pow(2, i, mod) if i != ln - 1 else x
            dp[i][j] = (dp[i-1][j-1] * d + dp[i-1][j]) % mod 
    print(dp[-1][-1])

if __name__ == '__main__':
    main()
    
"""
10 123456789

205695670
"""