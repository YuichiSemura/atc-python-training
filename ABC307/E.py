def main():

    MOD = 998244353
    n, m = map(int, input().split())
    ansl = [0] * n
    mil = [0] * n
    ansl[0] = m
    ansl[1] = m * (m-1) % 998244353
    mil[0] = (m-1)
    mil[1] = (m-1) * (m-1) % 998244353
    for i in range(2, n):
        mil[i] = (mil[i-1] * (m-1)) % MOD
        ansl[i] = (m * mil[i-1] - ansl[i-1]) % MOD
    print(ansl[-1])

if __name__ == '__main__':
    main()

"""

"""