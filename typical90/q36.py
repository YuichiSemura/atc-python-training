def main():

    n, q = map(int, input().split())
    nl = [list(map(int, input().split())) for _ in range(n)]
    ql = [int(input()) for _ in range(q)]
    xxl = [x+y for x, y in nl]
    yyl = [x-y for x, y in nl]
    xxlmax = max(xxl)
    xxlmin = min(xxl)
    yylmax = max(yyl)
    yylmin = min(yyl)
    for qq in ql:
        qq -= 1
        print(max(xxlmax - xxl[qq], xxl[qq]-xxlmin, yylmax - yyl[qq], yyl[qq] -yylmin))
    
if __name__ == '__main__':
    main()

"""
3 3
-1 2
1 1
-2 -3
1
2
3


"""