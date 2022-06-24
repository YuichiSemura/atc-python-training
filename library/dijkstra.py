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

    g = [
        [(5, 1, 1), (4, 2, 2), (1, 3, 3)],
        [(5, 0, 1), (2, 4, 4)],
        [(4, 0, 2), (2, 3, 5), (5, 4, 6), (6, 5, 7)],
        [(1, 0, 3), (2, 2, 5)],
        [(2, 1, 6), (5, 2, 6), (1, 6, 8), (3, 7, 9)],
        [(6, 2, 7), (2, 7, 10)],
        [(1, 4, 8), (4, 7, 11)],
        [(3, 4, 9), (2, 5, 10), (4, 6, 11)]
    ]

    dl, pl = dijkstra(0, g)
    print(dl)
    print(pl)
    pass


if __name__ == '__main__':
    main()
