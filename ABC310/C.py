def main():

    n = int(input())
    sl = [input() for _ in range(n)]
    ss = set()
    count = 0
    for s in sl:
        if s in ss or s[::-1] in ss:
            continue
        ss.add(s)
    print(len(ss))

if __name__ == '__main__':
    main()

"""
6
a
abc
de
cba
de
abc

"""