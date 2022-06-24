## ぴったり
A = [12, 39, 42, 57, 64, 88, 99]
bi = 42
st = 0
en = len(A)
while st + 1 != en:
    num = (st + en) // 2
    if A[num] > bi:
        en = num
    else:
        st = num
print(st, A[st])


## 小さいのが出る
A = [12, 39, 43, 57, 64, 88, 99]
bi = 51
st = 0
en = len(A)
while st + 1 != en:
    num = (st + en) // 2
    if A[num] > bi:
        en = num
    else:
        st = num
print(st, A[st])