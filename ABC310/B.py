def main():

    n, m = map(int, input().split())
    tmpl = [list(map(int, input().split())) for _ in range(n)]
    pcfl = [(l[0], l[1], set(l[2:]))for l in tmpl]
    pcfl.sort(key=lambda x: (x[0], x[1]))
    for i in range(n):
        for j in range(i+1, n):
            p1, c1, f_set1 = pcfl[i]
            p2, c2, f_set2 = pcfl[j]
            if p1 == p2:
                if f_set1 < f_set2 or f_set1 > f_set2:
                    print('Yes')
                    exit(0)
            elif f_set1 >= f_set2:
                print('Yes')
                exit(0)
            continue
    print("No")

if __name__ == '__main__':
    main()

"""
5 6
10000 2 1 3
15000 3 1 2 4
30000 3 1 3 5
35000 2 1 5
100000 6 1 2 3 4 5 6

2 2
100000 3 1 2
100000 3 1 2 4


2 2
90000 3 1 2 4
100000 3 1 2 4

"""