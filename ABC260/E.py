def main():

    n, m = map(int, input().split())
    abl = [list(map(int, input().split())) for _ in range(n)]
    invl = [[] for _ in range(m)]
    
    for ind, ab in enumerate(abl):
        a, b = ab[0], ab[1]
        invl[a-1].append(ind)
        invl[b-1].append(ind)
    
    result = [0 for _ in range(m+1)]
    now_count = [0 for _ in range(n)]
    st = 0
    ed = 1
    for c in invl[st]:
        now_count[c] += 1
    count = len(invl[st])
    while True:
        if count >= n:
            result[ed - st - 1] += 1
            result[m - st] -= 1
            for c in invl[st]:
                now_count[c] -= 1
                if now_count[c] == 0:
                    count -= 1
            st += 1
        else:
            if ed == m:
                break
            for c in invl[ed]:
                now_count[c] += 1
                if now_count[c] == 1:
                    count += 1
            ed += 1
    
    for i in range(0, m):
        result[i+1] = result[i+1] + result[i]
    
    print(' '.join([str(r) for r in result[:-1]]))
    
if __name__ == '__main__':
    main()
