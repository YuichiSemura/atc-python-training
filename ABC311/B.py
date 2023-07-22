def main():

    n, d = map(int, input().split())
    sl = [list(input()) for _ in range(n)]
    ans = []
    for i in range(d):
        c = [sl[j][i] == 'o' for j in range(n)]
        ans.append(all(c))
    count = 0
    mxc = 0
    for i in range(d):
        if ans[i]:
            count += 1
        else:
            count = 0
        mxc = max(mxc, count)
    # print(ans)
    print(mxc)

if __name__ == '__main__':
    main()

"""

"""