def main():

    n, k, q = map(int, input().split())
    al = list(map(int, input().split()))
    al = [a-1 for a in al]
    board = [0] * n
    for a in al:
        board[a] = 1
    ll = list(map(int, input().split()))
    ll = [l-1 for l in ll]
    for l in ll:
        if al[l] == n - 1:
            continue
        if board[al[l]+1] == 0:
            board[al[l]+1] = 1
            board[al[l]] = 0
            al[l] = al[l] + 1
            continue
    print(" ".join([str(a+1) for a in al]))

if __name__ == '__main__':
    main()
