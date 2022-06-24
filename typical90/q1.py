def main():

    N, L = map(int, input().split())
    K = int(input())
    A = list(map(int, input().split()))
    st = 1
    en = L // (K + 1) + 1
    num = st
    A.append(L)
    while st + 1 != en:
        num = (st + en) // 2
        ck = K + 1
        tmp = 0
        for i in A:
            if (i - tmp) >= num:
                tmp = i
                ck -= 1
        if ck > 0:
            en = num
        else:
            st = num
    print(st)

if __name__ == '__main__':
    main()
    
"""
3 34
1
8 13 26

3 34
2
8 13 26

3 34
3
8 13 26

13
---
7 45
2
7 11 16 20 28 34 38

12
---
20 1000
4
51 69 102 127 233 295 350 388 417 466 469 523 553 587 720 739 801 855 926 954

170
"""