def main():

    n, k = map(int, input().split())
    al = list(input().split())
    from collections import defaultdict
    
    st = 0
    ed = 0
    now_set = defaultdict(int)
    now_count = 0
    ans = 0
    while ed < n:
        ed += 1
        if now_set[al[ed - 1]] == 0:
            now_count += 1
        now_set[al[ed - 1]] += 1
        while now_count > k:
            if now_set[al[st]] == 1:
                now_count -= 1
            now_set[al[st]] -= 1
            st += 1
        ans = max(ans, ed - st)
    print(ans)

if __name__ == '__main__':
    main()

"""
5 1
1 2 3 4 5

5 4
1 1 2 4 2


"""