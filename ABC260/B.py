def main():
    from operator import itemgetter

    n, x, y, z = map(int, input().split())
    al = list(map(int, input().split()))
    bl = list(map(int, input().split()))
    ll = [[a, b, a+b, ind]for ind, (a, b) in enumerate(zip(al, bl))]
    ans = []
    ll = sorted(ll, key=lambda x: (x[0], -x[3]), reverse=True)
    ans.extend(ll[:x])
    ll = sorted(ll[x:], key=lambda x: (x[1], -x[3]), reverse=True)
    ans.extend(ll[:y])
    ll = sorted(ll[y:], key=lambda x: (x[2], -x[3]), reverse=True)
    ans.extend(ll[:z])
    ans.sort(key=itemgetter(3))
    for a in ans:
        print(a[3]+1)


if __name__ == '__main__':
    main()
