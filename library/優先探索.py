def main():
    from collections import deque
    n, m = list(map(int, input().split()))
    g = [[] for _ in range(n)]
    # 道リスト（x番目のml[x] = u, vを繋ぐ道）
    ml = []
    for i in range(m):
        mu, mv = list(map(int, input().split()))
        mu -= 1
        mv -= 1
        g[mu].append((mv, i))
        g[mv].append((mu, i))
        ml.append((mu, mv))

    # 深さ
    used = [False for _ in range(n)]
    q = deque()
    used[0] = True
    for nn in g[0]:
        q.append(nn)
    while(q):
        node, ed = q.pop()
        if used[node]:
            continue
        used[node] = True
        print(ml[ed][0]+1, ml[ed][1]+1)
        for nn in g[node]:
            q.append(nn)

    # 幅
    used = [False for _ in range(n)]
    q = deque()
    used[0] = True
    for nn in g[0]:
        q.append(nn)
    while(q):
        node, ed = q.popleft()
        if used[node]:
            continue
        used[node] = True
        print(ml[ed][0]+1, ml[ed][1]+1)
        for nn in g[node]:
            q.append(nn)


if __name__ == '__main__':
    main()


"""
input
6 8
5 1
4 3
1 4
3 5
1 2
2 6
1 6
4 2

output
1 4
4 3
5 3
4 2
6 2
1 5
5 3
1 4
2 1
1 6
"""
