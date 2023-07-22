n = int(input())
al = list(map(int, input().split()))
al = [0] + al
now = al[1]
ansl = set()
for _ in range(n):
    now = al[now]

ansl.add(now)
while True:
    now = al[now]
    if now in ansl:
        break
    ansl.add(now)
    
print(len(ansl))
print(*ansl)

"""
7
6 7 2 1 3 4 5

"""