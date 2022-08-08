import bisect


def main():

    n, k = map(int, input().split())
    pl = list(map(int, input().split()))
    ans = [-1] * n
    surface = []
    od = {}
    for turn, p in enumerate(pl, start=1):
        if len(surface) == 0 or surface[-1] < p:
            surface.append(p)
            od[str(p)] = [p]
        else:
            ind = bisect.bisect_left(surface, p)
            sf = surface[ind]
            od[str(p)] = od[str(sf)]
            od[str(p)].append(p)
            surface[ind] = p
            od[str(sf)] = None
            del od[str(sf)]
        # 食べられる
        if len(od[str(p)]) == k:
            ind = bisect.bisect_left(surface, p)
            surface.pop(ind)
            for i in od[str(p)]:
                ans[i-1] = turn
    
    for an in ans:
        print(an)


if __name__ == '__main__':
    main()
