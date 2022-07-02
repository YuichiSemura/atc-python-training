def main():

    n = int(input())
    s = list(str(input()))
    wl = list(map(int, input().split()))
    sl = [-1 if ss == '1' else 0 for ss in s]
    ll = [(w, s) for s, w in zip(sl, wl)]
    ll.sort()
    # print(ll)
    ol = []
    oc = 0
    kl = []
    kc = 0
    for w, s in ll:
        if s == -1:
            oc += 1
        if s == 0:
            kc += 1
        ol.append(oc)
        kl.append(kc)
    mx = ol[-1]
    for o, k in zip(ol, kl):
        # print(ol[-1] - o + k)
        mx = max(mx, ol[-1] - o + k)
    print(mx)

if __name__ == '__main__':
    main()

"""
9

30 35 40 40 60 80
40 43 45

50 60 60
50 50
"""