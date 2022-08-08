def main():

    n, c = map(int, input().split())
    m = 2 ** 30 - 1
    s1 = m
    s0 = 0
    for _ in range(n):

        t, a = map(int, input().split())
        if t == 1:
            s1 &= a
            s0 &= a
        elif t == 2:
            s1 |= a
            s0 |= a
        else:
            s1 ^= a
            s0 ^= a
        c = (c & s1) | ((c ^ m) & s0)
        print(c)


if __name__ == '__main__':
    main()
