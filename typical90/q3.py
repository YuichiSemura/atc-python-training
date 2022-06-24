def main():

    from collections import deque
    import heapq
    N = int(input())
    g = [[] for _ in list(range(N))]
    used = [False for _ in range(N)]
    jun = []
    mnl = [[0, 0] for _ in list(range(N))]
    for _ in list(range(N-1)):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
        g[ai].append(bi)

    # 深さ
    used = [False for _ in range(N)]
    q = deque()
    used[0] = True
    jun.append(0)
    for nn in g[0]:
        q.append(nn)
    while(q):
        node = q.pop()
        if used[node]:
            continue
        jun.append(node)
        used[node] = True
        for nn in g[node]:
            q.append(nn)

    # print("---")
    for j in reversed(jun):
        if len(g[j]) == 0:
            mnl[j] = [0, 0]
        else:
            x = [mnl[nn][0] + 1 for nn in g[j]]
            if len(g[j]) == 1:
                mnl[j] = [max(x), 0]
            else:
                mnl[j] = heapq.nlargest(2, x)
        # print(j, mnl[j])
    print(max([sum(mn) for mn in mnl]) + 1)


if __name__ == '__main__':
    main()

"""
31
1 2
1 3
2 4
2 5
3 6
3 7
4 8
4 9
5 10
5 11
6 12
6 13
7 14
7 15
8 16
8 17
9 18
9 19
10 20
10 21
11 22
11 23
12 24
12 25
13 26
13 27
14 28
14 29
15 30
15 31

9
"""