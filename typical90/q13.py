def dijkstra(s: int, g: list):
    
    from heapq import heappush, heappop
    dl = [0 if node == s else -1 for node in range(len(g))]
    pl = [() for a in range(len(g))]
    cl = [False for a in range(len(g))]
    q = []
    for d, v, ed in g[s]:
        heappush(q, (d, v))
        dl[v] = d
        pl[v] = (s, ed)
    while q:
        d, v = heappop(q)
        if cl[v]: continue
        cl[v] = True
        for ud, uv, ed in g[v]:
            alt = ud + d
            if -1 == dl[uv] or not cl[uv] and alt < dl[uv]:
                dl[uv] = alt
                heappush(q, (alt, uv))
                pl[uv] = (v, ed)
    return dl, pl

def main():

    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for i in range(m):
        a, b, c = map(int, input().split())
        g[a-1].append((c, b-1, i))
        g[b-1].append((c, a-1, i))
    dl1, pl1 = dijkstra(0, g)
    dln, pln = dijkstra(n-1, g)
    for i in range(n):
        print(dl1[i]+dln[i])

if __name__ == '__main__':
    main()
