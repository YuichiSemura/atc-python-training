def main():

    from collections import deque
    N = int(input())
    g = [[] for _ in list(range(N))]
    for _ in list(range(N-1)):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
        g[ai].append(bi)
        g[bi].append(ai)

    # 深さ
    q = deque()
    dl = [-1 for _ in range(N)]
    dl[0] = 0
    for nn in g[0]:
        q.append((nn, 0))
    while(q):
        node, parent = q.pop()
        if dl[node] != -1:
            continue
        dl[node] = dl[parent] + 1
        for nn in g[node]:
            q.append((nn, node))

    mx = 0
    mxind = -1
    for i, d in enumerate(dl):
        if d > mx:
            mxind = i

    q = deque()
    dl2 = [-1 for _ in range(N)]
    dl2[mxind] = 0
    for nn in g[mxind]:
        q.append((nn, mxind))
    while(q):
        node, parent = q.pop()
        if dl2[node] != -1:
            continue
        dl2[node] = dl2[parent] + 1
        for nn in g[node]:
            q.append((nn, node))

    # print(dl)
    # print(dl2)
    print(max(dl2)+1)


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