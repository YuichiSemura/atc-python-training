mod = 998244353
memo_max = 3 * 10 ** 5
fact = [1] * memo_max
inv = [1] * memo_max
f_inv = [1] * memo_max
for i in range(2, memo_max):
    fact[i] = fact[i - 1] * i % mod
    inv[i] = mod - inv[mod % i] * (mod // i) % mod
    f_inv[i] = f_inv[i - 1] * inv[i] % mod

def P(n, r):
    if n < r:
        return 0
    else:
        return fact[n] * f_inv[n-r] % mod

def C(n, r):
    if n < r:
        return 0
    else:
        return (fact[n] * f_inv[r] % mod) * f_inv[n-r] % mod

def main():
    
    n, m, k = map(int, input().split())
    gl = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        gl[u-1].append(v-1)
        gl[v-1].append(u-1)
    oddlen = len([1 for ll in gl if len(ll) % 2 == 1])
    evenlen = n - oddlen
    ct = 0
    i = 0
    while i * 2 <= k:
        k_even = k - i * 2
        k_odd = i * 2
        ct += C(evenlen, k_even) * C(oddlen, k_odd)
        ct %= mod
        i += 1
    print(ct)


if __name__ == '__main__':
    main()
