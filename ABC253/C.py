from collections import defaultdict
import heapq
def main():

    q = int(input())
    dc = defaultdict(int)
    mxq = []
    mnq = []
    for _ in range(q):
        ql = list(map(int, input().split()))
        if ql[0] == 1:
            dc[str(ql[1])] += 1
            heapq.heappush(mxq, -ql[1])
            heapq.heappush(mnq, ql[1])
        elif ql[0] == 2:
            dc[str(ql[1])] = max(0, dc[str(ql[1])]- ql[2])
        elif ql[0] == 3:
            mx = heapq.heappop(mxq)
            while dc[str(-mx)] == 0:
                mx = heapq.heappop(mxq)
            heapq.heappush(mxq, mx)
            mn = heapq.heappop(mnq)
            while dc[str(mn)] == 0:
                mn = heapq.heappop(mnq)
            heapq.heappush(mnq, mn)
            print(-mx-mn)

if __name__ == '__main__':
    main()
