from math import atan2, degrees

def main():
    
    n = int(input())
    l = [list(map(int, input().split())) for _ in range(n)]
        
    ans = 0
    for ind, c in enumerate(l):
        
        nl = [degrees(atan2(a[0]-c[0], a[1]-c[1])) for jnd, a in enumerate(l) if ind != jnd]
        nl.sort()
        # print(nl)
        
        i = 1
        j = 0
        while i < n - 1:
            c = nl[i] - nl[j]
            # print(nl[i], nl[j], c, 360-c)
            ans = max(ans, min(c, 360-c))
            if nl[i] - nl[j] < 180:
                i += 1
            else:
                j += 1
    print(ans)
        
if __name__ == '__main__':
    main()
