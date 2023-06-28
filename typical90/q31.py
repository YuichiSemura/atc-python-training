# Grundy数
# わからない
def main():

    n = int(input())
    wl = list(map(int, input().split()))
    bl = list(map(int, input().split()))
    
    wmax = 51
    bmax = 1326
    grl =[[-1] * bmax for _ in range(wmax)]
    for w in range(0, wmax):
        for b in range(1, bmax):
            nl = []
            if b > 1:
                nl.extend(grl[w][(b+1)//2:b])
            if w >= 1 and w + b < bmax:
                nl.append(grl[w-1][w+b])
            grl[w][b] = mex(nl)
    ans = 0
    for w, b in zip(wl, bl):
        ans ^= grl[w][b]
    print("Second" if ans == 0 else "First")
    
def mex(l):
    
    s = set(l)
    for i in range(10**9):
        if i not in s:
            return i
    return len(l)

if __name__ == '__main__':
    main()

"""
2
10 10
10 10

6          
1 2 3 4 5 6
1 2 3 4 5 6

"""