def main():

    n, m = map(int, input().split())
    abl = [list(map(int, input().split())) for _ in range(m)]
    g = [[] for _ in range(n)]
    for ab in abl:
        a, b = ab[0]-1, ab[1]-1
        g[b].append(a)
    
    if [len(gg) for gg in g].count(0) != 1:
        print(-1)
        exit(0)
    for ind, gg in enumerate(g):
        if len(gg) == 0:
            ft = ind
            break
    
    from collections import deque
    g = [[] for _ in range(n)]
    for ab in abl:
        a, b = ab[0]-1, ab[1]-1
        g[a].append(b)
    used = [False] * n
    q = deque()
    used[ft] = True
    for nn in g[ft]:
        q.append(nn)
    while q:
        node = q.pop()
        if used[node]:
            continue
        used[node] = True
        for nn in g[node]:
            q.append(nn)
    print(ft+1 if all(used) else -1)
    

if __name__ == '__main__':
    main()

"""

"""