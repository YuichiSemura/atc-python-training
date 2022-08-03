
def main():

    n = int(input())
    sx, sy, tx, ty = map(int, input().split())
    stl = [tuple(map(int, input().split())) for _ in range(n)]
    
    inds = -1
    indt = -1
    for indi, (ax, ay, ar) in enumerate(stl):
        if inds == -1 and ((sx - ax) ** 2 + (sy - ay) ** 2  == ar ** 2):
            inds = indi
        if indt == -1 and ((tx - ax) ** 2 + (ty - ay) ** 2  == ar ** 2):
            indt = indi
    
    if inds == indt:
        print("Yes")
        return
    
    g = [[] for _ in range(n)]
    for indi, (ax, ay, ar) in enumerate(stl):
        for indj, (bx, by, br) in enumerate(stl):
            if indi >= indj:
                continue
            if abs(ar - br) ** 2 <= (ax - bx) ** 2 + (ay - by) ** 2 <= (ar + br) ** 2:
                g[indi].append(indj)
                g[indj].append(indi)
    
    # 深さ
    from collections import deque
    used = [False for _ in range(n)]
    q = deque()
    used[inds] = True
    for nn in g[inds]:
        q.append(nn)
    while(q):
        node = q.pop()
        if used[node]:
            continue
        used[node] = True
        for nn in g[node]:
            q.append(nn)
    print("Yes" if used[indt] else "No")

if __name__ == '__main__':
    main()
