def main():

    al = list(map(int, input().split()))
    hl = al[:3]
    wl = al[3:]
    if sum(hl) != sum(wl):
        print(0)
        return
    count = 0
    hl.sort()
    wl.sort()
    x = min(hl[0], wl[0])
    y = min(hl[0], wl[1])
    z = min(hl[1], wl[0])
    w = min(hl[1], wl[1])
    for a in range(1, x):
        for b in range(1, y):
            for d in range(1, z):
                for e in range(1, w):
                    c = hl[0] - a - b
                    f = hl[1] - d - e
                    g = wl[0] - a - d
                    h = wl[1] - b - e
                    i = wl[2] - c - f
                    if c > 0 and f > 0 and g > 0 and h > 0 and i > 0:
                        count+=1
    print(count)

if __name__ == '__main__':
    main()

"""
5 13 10 6 13 9

120
"""
