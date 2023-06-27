from itertools import permutations

def main():

    n = int(input())
    al = [list(map(int, input().split())) for _ in range(n)]
    m = int(input())
    ng = [[True] * n for _ in range(n)] 
    for _ in range(m):
        x, y = map(int, input().split())
        ng[x-1][y-1] = False
        ng[y-1][x-1] = False
    min_cost = 10 ** 18
    for perm in permutations(range(0, n)):
        prev = perm[0]
        cost = al[prev][0]
        bk = False
        for ind, p in enumerate(perm[1:]):
            if not ng[prev][p]:
                bk = True
                break
            cost += al[p][ind+1]
            prev = p
        if bk:
            continue
        min_cost = min(min_cost, cost)
    print(min_cost if min_cost < 10 ** 18 else -1)
    
if __name__ == '__main__':
    main()

"""

"""