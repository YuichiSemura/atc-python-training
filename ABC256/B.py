def main():

    n = int(input())
    al = list(map(int, input().split()))
    
    from collections import deque
    
    q = deque()
    q.append(False)
    q.append(False)
    q.append(False)
    p = 0
    for a in al:
        for b in range(a):
            if q.pop():
                p += 1
            q.appendleft(b == 0)
    print(p)

if __name__ == '__main__':
    main()
