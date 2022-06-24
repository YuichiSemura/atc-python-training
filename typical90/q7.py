def main():

    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    A.sort()
    # print(A)
    for _ in range(Q):
        bi = int(input())
        if A[0] >= bi:
            print(A[0] - bi)
            continue
        elif A[-1] <= bi:
            print(bi - A[-1])
            continue
        st = 0
        en = N
        while st + 1 != en:
            num = (st + en) // 2
            if A[num] > bi:
                en = num
            else:
                st = num
        # print("--", A[st], bi, A[st]<bi)
        print(min(bi - A[st], A[st+1] - bi))

if __name__ == '__main__':
    main()
    
"""
4
4000 4400 5000 3200
3
3312
2992
4229

"""