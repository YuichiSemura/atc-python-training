def main():

    n, a, b = map(int, input().split())
    md = euclidean(a, b)
    c = a * b // md
    na = n // a
    nb = n // b
    nc = n // c
    print(n * (n + 1) // 2 - na * (na + 1) // 2 * a - nb * (nb + 1) // 2 * b + nc * (nc + 1) // 2 * c)

def euclidean(n: int, m: int):
    
    while True:
        n = n % m
        if n == 0:
            return m
        m, n = n, m

if __name__ == '__main__':
    main()
