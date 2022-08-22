import bisect


def main():

    n, p, q, r = map(int, input().split())
    al = list(map(int, input().split()))
    suml = [0] * (n+1)
    for ind, a in enumerate(al):
        suml[ind+1] = suml[ind] + a

    for x, _ in enumerate(suml[:-3]):
        y = bisect.bisect_left(suml, suml[x] + p)
        if y > n:
            continue
        z = bisect.bisect_left(suml, suml[y] + q)
        if z > n:
            continue
        w = bisect.bisect_left(suml, suml[z] + r)
        if w > n:
            continue
        if suml[y]-suml[x] == p and suml[z]-suml[y] == q and suml[w]-suml[z] == r:
            print("Yes")
            return
    print("No")


if __name__ == '__main__':
    main()
