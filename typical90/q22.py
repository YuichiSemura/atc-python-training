def main():

    a, b, c = map(int, input().split())
    gcd = euclidean(euclidean(a, b), euclidean(b, c))
    print(a // gcd + b // gcd + c // gcd - 3)

def euclidean(n: int, m: int):
    
    while True:
        n = n % m
        if n == 0:
            return m
        m, n = n, m


if __name__ == '__main__':
    main()

"""

"""