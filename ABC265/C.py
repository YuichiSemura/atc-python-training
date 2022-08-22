def main():

    h, w = map(int, input().split())
    flgl = [[False for _ in range(w)] for _ in range(h)]
    gl = [list(input()) for _ in range(h)]
    nh, nw = 0, 0
    while True:
        if flgl[nh][nw]:
            print("-1")
            return
        flgl[nh][nw] = True
        if gl[nh][nw] == "U":
            if nh == 0:
                break
            else:
                nh = nh - 1
        elif gl[nh][nw] == "D":
            if nh == h-1:
                break
            else:
                nh = nh + 1
        elif gl[nh][nw] == "L":
            if nw == 0:
                break
            else:
                nw = nw - 1
        elif gl[nh][nw] == "R":
            if nw == w-1:
                break
            else:
                nw = nw + 1
    print(nh+1, nw+1)


if __name__ == '__main__':
    main()
