def main():

    from math import gcd
    n, m = map(int, input().split())
    lcm = n * m // gcd(n, m)
    print(lcm if lcm <= 10**18 else "Large")

if __name__ == '__main__':
    main()

"""

"""