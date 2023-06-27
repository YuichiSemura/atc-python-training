# 逆元
mod = 10 ** 9 + 7
n = int(input())
memo_max = 2 * 10 ** 5
fact = [1] * memo_max
inv = [1] * memo_max
f_inv = [1] * memo_max

for i in range(2, memo_max):
    fact[i] = fact[i - 1] * i % mod
    inv[i] = mod - inv[mod % i] * (mod // i) % mod
    f_inv[i] = f_inv[i - 1] * inv[i] % mod

def P(n, r, mod=10**9+7):
    if n < r:
        return 0
    else:
        return fact[n] * f_inv[n-r] % mod

def C(n, r, mod=10**9+7):
    if n < r:
        return 0
    else:
        return (fact[n] * f_inv[r] % mod) * f_inv[n-r] % mod


for k in range(1, n+1):
    i = 1
    count = 0
    while i < n + 1 and n - (i - 1) * (k - 1) > 0:
        count = (count + C(n - (i - 1) * (k - 1), i, mod)) % mod
        i += 1
    print(count)

"""

"""