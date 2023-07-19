import sys
sys.setrecursionlimit(10 ** 7)

n, t, m = map(int, input().split())
ngl = [[] for _ in range(n)]
ql = [list(map(int, input().split())) for _ in range(m)]
for q in ql:
    ngl[q[0] - 1].append(q[1] - 1)
    ngl[q[1] - 1].append(q[0] - 1)
# 一時的なリスト
tt = []

def tansaku(i):
    if i == n:
        if len(tt) != t:
            return 0
        return 1
    count = 0
    for teamcount in range(len(tt)):
        if any([check in tt[teamcount] for check in ngl[i]]):
            continue
        tt[teamcount].add(i)
        count += tansaku(i+1)
        tt[teamcount].remove(i)
    if len(tt) < t:
        tt.append(set())
        tt[-1].add(i)
        count += tansaku(i+1)
        tt[-1].remove(i)
        tt.pop()
    return count

print(tansaku(0))

"""
5 2 2
1 3
3 4

"""