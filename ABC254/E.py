def main():
    
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in list(range(m)):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
        g[ai].append(bi)
        g[bi].append(ai)

    q = int(input())
    used = [False for _ in list(range(n))]
    for _ in list(range(q)):
        xi, ki = map(int, input().split())
        check(xi-1, ki, g, used)
        

def check(x, k, g, used):

    from collections import deque
    # 幅
    ans = [x+1]
    q = deque()
    used[x] = True
    for nn in g[x]:
        q.append((nn, 1))
    while(q):
        node, d = q.popleft()
        # print("  ", node+1, d, k, used[node])
        if used[node] or d > k:
            continue
        used[node] = True
        ans.append(node+1)
        # print(node+1)
        if d != k:
            for nn in g[node]:
                q.append((nn, d+1))
    # print(ans)
    for a in ans:
        used[a-1] = False
    print(sum(ans))

if __name__ == '__main__':
    main()
    
"""
6 5
2 3
3 4
3 5
5 6
2 6
1
2 3
"""