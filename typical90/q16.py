def main():

    n = int(input())
    a, b, c = map(int, input().split())
    a, b, c = min(a, b, c), a+b+c-min(a, b, c)-max(a, b, c), max(a, b, c)
    x = n % c
    mn = 10000
    while x <= n:
        y = x % b
        while y <= x:
            if y % a == 0:
                mn = min(mn, (x-y) // b + y // a + (n-x) // c)
            y += b
        x += c
    print(mn)


if __name__ == '__main__':
    main()
