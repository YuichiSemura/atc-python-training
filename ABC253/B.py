def main():

    h, w = map(int, input().split())
    kl = []
    for i in range(h):
        s = str(input())
        for j, a in enumerate(s):
            if a == 'o':
                kl.append([i, j])
    print(abs(kl[0][0]-kl[1][0])+abs(kl[0][1]-kl[1][1]))

if __name__ == '__main__':
    main()
