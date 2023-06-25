def main():

    n = int(input())
    pl = list(map(int, input().split()))
    ql = list(map(int, input().split()))
    blc = [0] * (2 * n)
    mx = 0
    for i in list(range(2 * n)):
        if mx > pl[i]:
            if blc[mx-1] == -1 or blc[pl[i]-1] == 1:
                return -1
            blc[mx-1], blc[pl[i]-1] = 1, -1
        else:
            mx = pl[i]
    # print(blc)
    mn = 2 * n
    for i in list(range(2 * n)):
        if mn < ql[i]:
            if blc[mn-1] == -1 or blc[ql[i]-1] == 1:
                return -1
            blc[mn-1], blc[ql[i]-1] = 1, -1
        else:
            mn = ql[i]
    # print(blc)
    for b in blc:
        if b == 0:
            return -1
    ll = [ind for ind, b in enumerate(blc) if b == 1]
    rl = [ind for ind, b in enumerate(blc) if b == -1]
    if len(ll) != n or len(rl) != n:
        return -1
    checkcount = 0
    for pa in pl:
        checkcount += blc[pa-1]
        if checkcount < 0:
            return -1
    checkcount = 0
    for qa in ql:
        checkcount += blc[qa-1]
        if checkcount < 0:
            return -1
    return ''.join(['(' if b == 1 else ')' for b in blc])


if __name__ == '__main__':
    print(main())


"""
2 
1 3 2 4
2 4 1 3

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
