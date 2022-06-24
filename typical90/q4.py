def main():

    h, w = map(int, input().split())
    g = []
    nl = list(range(h))
    ml = list(range(w))
    hl = []
    wl = [0] * w
    for i in nl:
        a = list(map(int, input().split()))
        g.append(a)
        hl.append(sum(a))
        for j in ml:
            wl[j] += a[j]
    for i, hli in enumerate(hl):
        print(" ".join([str(hli + wl[j] - g[i][j]) for j in ml]))

if __name__ == '__main__':
    main()