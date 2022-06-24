def main():

    x, a, d, n  = map(int, input().split())
    if d < 0:
        a = a + d * (n-1)
        d = -d
    ma = a + d * (n-1)
    if x < a:
        print(a-x)
    elif x < ma:
        y = (x-a) % d
        print(min(y, d-y))
    else:
        print(x-ma)

if __name__ == '__main__':
    main()
