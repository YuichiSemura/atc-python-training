from itertools import combinations

def main():

    h1, w1 = map(int, input().split())
    al = [list(map(int, input().split())) for _ in range(h1)]
    h2, w2 = map(int, input().split())
    bl = [list(map(int, input().split())) for _ in range(h2)]

    def check(hl, wl):
        
        for indh, h in enumerate(hl):
            for indw, w in enumerate(wl):
                if al[h][w]!=bl[indh][indw]:
                    return False
        return True

    for hl in combinations(range(h1), h2):
        for wl in combinations(range(w1), w2):
            if check(hl, wl):
                print("Yes")
                exit()
    print("No")

if __name__ == '__main__':
    main()
