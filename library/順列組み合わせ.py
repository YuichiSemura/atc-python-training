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
