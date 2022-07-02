def main():

    n, x = map(int, input().split())
    l = [list(map(int, input().split())) for _ in range(n)]
    a = 0
    mn = 10 ** 30
    for ind, ll in enumerate(l):
        if x - ind == 0:
            break
        b = a + ll[0] + ll[1] * (x - ind)
        a = a + ll[0] + ll[1]
        mn = min(mn, b)
    print(mn)
    
if __name__ == '__main__':
    main()

"""
10 6
3 3
1 6
4 7
1 8
5 7
9 9
2 4
6 4
5 2
3 1

"""