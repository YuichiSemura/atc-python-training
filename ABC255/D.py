def main():

    n, q = map(int, input().split())
    al = list(map(int, input().split()))
    al.sort()
    s = 0
    sl = []
    for a in al:
        s += a
        sl.append(s)
    
    for _ in range(q):
        x = int(input())
        if x < al[0]:
            print(sl[-1] - x * len(al))
            continue
        st = 0
        en = len(al)
        while st + 1 != en:
            num = (st + en) // 2
            if al[num] > x:
                en = num
            else:
                st = num
        print((st + 1) * x - sl[st] + sl[-1] - sl[st] - (len(al) - st - 1) * x)
    
if __name__ == '__main__':
    main()
