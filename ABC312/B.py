def main():

    n, m = map(int, input().split())
    sl = [[ss == "#" for ss in list(input())] for _ in range(n)]
    for i in range(n-8):
        for j in range(m-8):
            if not dou(sl, i, j):
                continue
            print(i+1, j+1)
            
def dou(sl, i, j):
    
    for ii in range(3):
        for jj in range(3):
            if not sl[i+ii][j+jj]:
                return False
            if not sl[i+6+ii][j+6+jj]:
                return False
    for x in range(4):
        if sl[i+x][j+3]:
            return False
        if sl[i+3][j+x]:
            return False
        if sl[i+5+x][j+5]:
            return False
        if sl[i+5][j+5+x]:
            return False
    return True

if __name__ == '__main__':
    main()

"""

"""