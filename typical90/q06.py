def main():

    n, k = map(int, input().split())
    sl = input()
    dp = [[n] * 26 for _ in range(n)]
    r26 = [i for i in range(26)]
    dp[-1][ord(sl[-1]) - ord('a')] = n-1
    nr = reversed([i for i in range(n-1)])
    for i in nr:
        h = dp[i]
        for j in r26:
            h[j] = dp[i+1][j]
        h[ord(sl[i]) - ord('a')] = i
    
    ans = []
    i = 0
    count = 0
    while count < k:
        # print("i", i)
        # print("count", count)
        for j in r26:
            if dp[i][j] + k - count - 1 < n:
                ans.append(chr(j + ord('a')))
                # print("ndp", dp[i][j])
                i = dp[i][j] + 1
                count += 1
                break
    
    # for d in dp:
    #     print(d)
    
    print("".join(ans))


if __name__ == '__main__':
    main()
    
"""    
r
    atcoder
    1999999
    3339999
    5555599
    6666669
    4444999
    7777777
    2299999
    acd
    
7 3
atcoder
"""