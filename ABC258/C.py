def main():

    from collections import deque
    n, q = map(int, input().split())
    s = list(input())
    ind = 0
    for i in range(q):
        t, x = map(int, input().split())
        if t == 1:
            ind = (ind - x) % n
        else:
            print(s[(ind + x - 1) % n])

if __name__ == '__main__':
    main()
