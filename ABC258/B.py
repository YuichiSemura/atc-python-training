def main():

    n = int(input())
    al = [list(str(input())) for _ in range(n)]
    mxx = 0
    ans = []
    for i in range(n):
        for j in range(n):
            for k in [-1, 0, 1]:
                for l in [-1, 0, 1]:
                    if k == 0 and l == 0:
                        continue
                    ans = []
                    for m in range(1, n+1):
                        ans.append(al[(i-1+k*m)%n][(j-1+l*m)%n])
                    sm = int("".join(ans))
                    mxx = max(mxx, sm)
    print(mxx)

if __name__ == '__main__':
    main()
