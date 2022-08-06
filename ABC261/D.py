def main():

    n, l, r = map(int, input().split())
    al = list(map(int, input().split()))
    ct = 0

    suml = [0]
    for a in al:
        ct += a
        suml.append(ct)

    sumr = [suml[-1]]
    for a in suml[:-1]:
        sumr.append(suml[-1] - a)
    sumr.append(0)

    mnl = [0] * (n+1)
    for ind in range(1, n+1):
        mnl[ind] = min(mnl[ind-1] + al[ind-1], l * ind)

    mxl = [0] * (n+1)
    for ind in range(n, 0, -1):
        mxl[ind-1] = min(mxl[ind] + al[ind-1], r * (n + 1 - ind))
    
    rl = [n + x for n, x in zip(mnl, mxl)]
    print(min(rl))


if __name__ == '__main__':
    main()
