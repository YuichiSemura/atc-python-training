def main():

    n = int(input())
    l = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if j == n - 1 and j % 2 == 0:
                l[i][j] = i * n + j + 1
            else:
                l[i][j] = i * n + (j // 2 * 2) + 2 - j % 2
    
    print("\n".join([" ".join([str(j) for j in i]) for i in l]))

if __name__ == '__main__':
    main()
