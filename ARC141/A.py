def main():

    for _ in range(int(input())):
        M = input().rstrip()
        ln = len(M)
        l = [i for i in range(1, ln) if ln % i == 0]
        cycle = [10 ** (ln-1) - 1]
        for i in l:
            di = sum([10 ** (k*i) for k in range(ln // i)])
            nn = int(M) // di * di
            cycle.append(nn)
        print(max(cycle))

if __name__ == '__main__':
    main()
