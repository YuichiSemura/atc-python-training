def main():
    import math
    n = int(input())
    l = [i+1 for i in list(range(n))]
    r = math.floor(math.sqrt(n))
    for k in range(2, r + 1):
        for i in list(range(n)):
            while(l[i] % (k*k) == 0):
                l[i] //= (k*k)
    cnt = [0 for _ in range(n)]
    ans = 0
    for i in l:
        cnt[i-1] += 1
    for c in cnt:
        ans += c*c
    print(ans)


if __name__ == '__main__':
    main()