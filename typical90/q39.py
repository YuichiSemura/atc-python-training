import sys
sys.setrecursionlimit(10 ** 7)

def DFS(g, cnt, start, stop):
  
  ret = 1
  for i in g[start]:
    if i != stop:
      ret += DFS(g, cnt, i, start)
  cnt[start] = ret
  return ret

def main():

    n = int(input())
    from collections import deque
    # グラフ g[u] = [(v, edge_id), ...]
    g = [[] for _ in range(n)]
    # 道リスト（x番目のml[x] = u, vを繋ぐ道）
    ml = []
    for i in range(n-1):
        mu, mv = map(int, input().split())
        mu -= 1
        mv -= 1
        g[mu].append(mv)
        g[mv].append(mu)
        ml.append((mu, mv))
    cnt=[-1 for i in range(n)]
    DFS(g, cnt, 0, -1)
    ans = 0
    print(cnt)
    for u, v in ml:
        ans += min(cnt[u], cnt[v]) * (n - min(cnt[u], cnt[v]))
    print(ans)
    

if __name__ == '__main__':
    main()

"""
4
1 2
1 3
1 4

12
1 2
3 1
4 2
2 5
3 6
3 7
8 4
4 9
10 5
11 7
7 12


"""