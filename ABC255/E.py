def main():
    
    n, m = map(int, input().split())
    sl = list(map(int, input().split()))
    xl = list(map(int, input().split()))
    bl = [0]
    for s in sl:
        bl.append(s - bl[-1])
        
    from collections import defaultdict
    m = defaultdict(int)
    for i, b in enumerate(bl):
        for j, x in enumerate(xl):
            m[str((-1) ** (i+1) * (x - b))] += 1
    
    mx = 0
    for v in m.values():
        mx = max(mx, v)
    print(mx)

if __name__ == '__main__':
    main()

"""
9 2
2 3 3 4 -4 -7 -4 -1
-1 5

3,−1,4,−1,5,−9,2,−6,5
2, 0,3, 0,4,-8,1,-5,4
0, 2, 1, 
"""