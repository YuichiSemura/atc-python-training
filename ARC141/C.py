def main():

    n = int(input())
    pl = list(map(int, input().split()))
    ql = list(map(int, input().split()))
    blc = [-1] * (2 * n)
    for i in list(range(2 * n - 1)):
        if pl[i] > pl[i+1]:
            blc[pl[i]-1] = 0
            blc[pl[i+1]-1] = 1
    for i in list(range(2 * n - 1)):
        if ql[i] < ql[i+1]:
            if blc[ql[i]-1] == 1 or blc[ql[i+1]-1] == 0:
                return -1
            blc[ql[i]-1] = 0
            blc[ql[i+1]-1] = 1
    for b in blc:
        if b == -1:
            return -1
    if blc.count(1) != n:
        return -1
    return ''.join(['(' if b == 0 else ')' for b in blc])


if __name__ == '__main__':
    print(main())

"""
4 
2 1 4 3 5 6 7 8
7 8 5 6 4 3 2 1
)()(()()

4 
2 1 4 5 3 6 7 8
7 8 5 6 4 3 2 1
-1

4
1 2 3 4 5 6 7 8
7 8 3 6 2 5 1 4
((()))()

4
4 1 5 3 6 2 8 7
8 7 6 5 4 3 2 1
)))((()(
    
1 8 7 2 6 4 3 5
"""
