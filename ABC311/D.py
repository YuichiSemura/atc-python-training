def main():

    n, m = map(int, input().split())
    sl = [[s == '.' for s in list(input())] for _ in range(n)]
    ans = [[False for _ in range(m)] for _ in range(n)]
    done = [[False for _ in range(m)] for _ in range(n)]
    
    nowi, nowj = 1, 1
    queue = [(1, 1)]
    while len(queue) > 0:
        nowi, nowj = queue[0]
        queue = queue[1:]
        if done[nowi][nowj]:
            continue
        # print(nowi, nowj)
        done[nowi][nowj] = True
        # 右
        i, j = nowi, nowj
        while sl[i][j]:
            ans[i][j] = True
            j += 1
        if not done[i][j-1]:
            queue.append((i, j-1))
        # 左
        i, j = nowi, nowj
        while sl[i][j]:
            ans[i][j] = True
            j -= 1
        if not done[i][j+1]:
            queue.append((i, j+1))
        # 上
        i, j = nowi, nowj
        while sl[i][j]:
            ans[i][j] = True
            i += 1
        if not done[i-1][j]:
            queue.append((i-1, j))
        # 左
        i, j = nowi, nowj
        while sl[i][j]:
            ans[i][j] = True
            i -= 1
        if not done[i+1][j]:
            queue.append((i+1, j))
    # for i in range(n):
    #     print("".join(['T' if aa else 'F' for aa in ans[i]]))
    print(sum([a.count(True) for a in ans]))
    

if __name__ == '__main__':
    main()

"""
6 6
######
#....#
#.#..#
#..#.#
#....#
######

"""