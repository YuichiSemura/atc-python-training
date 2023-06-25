from collections import deque

def main():

    _ = int(input())
    s = input()
    q = deque()
    dl = []
    for ind, ss in enumerate(s):
        if ss == '(':
            q.append(ind)
        if ss == ')':
            if len(q) > 0:
                v = q.pop()
                dl.append((v, ind))
    dl.sort()
    nowli = -1
    nowri = -1
    newd = []
    # print(dl)
    for li, ri in dl:
        if li > nowri and ri > nowri:
            if nowli != -1:
                newd.append((nowli, nowri))
            nowli, nowri = li, ri
    if nowli != -1:
        newd.append((nowli, nowri))
    # print(newd)
    for li, ri in reversed(newd):
        s = s[:li]+s[ri+1:]
    print(s)

if __name__ == '__main__':
    main()

"""

"""