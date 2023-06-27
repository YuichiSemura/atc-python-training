# 深さ優先探索

def main():

    from collections import deque
    n = int(input())
    abl = [map(int, input().split()) for _ in range(n-1)]
    g = [[] for _ in range(n)]
    for a, b in abl:
        g[a-1].append(b-1)
        g[b-1].append(a-1)
    used = [-1] * n
    pairs = [[], []]
    q = deque()
    q.append(0)
    used[0] = 0
    pairs[0].append(str(1))
    while q:
        node = q.pop()
        for nv in g[node]:
            if used[nv] != -1:
                continue
            q.append(nv)
            used[nv] = 1 - used[node]
            pairs[used[nv]].append(str(nv+1))
    if len(pairs[0]) >= len(pairs[1]):
        print(" ".join(pairs[0][:(n//2)]))
    else:
        print(" ".join(pairs[1][:(n//2)]))


if __name__ == '__main__':
    main()

"""
6
1 3
2 4
2 5
3 5
3 6

6
1 2
2 3
3 4
4 5
5 6

6
6 5
5 4
4 3
3 2
2 1

"""