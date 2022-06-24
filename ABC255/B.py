def main():

    from math import sqrt
    n, k = map(int, input().split())
    al = list(map(int, input().split()))
    al = [a-1 for a in al]
    nal = [False] * n
    for a in al:
        nal[a] = True
    nal = [index for index, na in enumerate(nal) if not na]
    
    mx = 0
    xyl = [list(map(int, input().split())) for _ in range(n)]
    for na in nal:
        mxx = 1000000000000 * 2
        for a in al:
            mxx = min(mxx, sqrt((xyl[na][0] - xyl[a][0]) ** 2 + (xyl[na][1] - xyl[a][1]) ** 2))
        mx = max(mx, mxx)
    print(mx)
    
if __name__ == '__main__':
    main()
