def main():

    N, M, X, T, D = map(int, input().split())
    print(T - max(0, X - M) * D)

if __name__ == '__main__':
    main()
