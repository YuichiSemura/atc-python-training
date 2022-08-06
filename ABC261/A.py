from email.policy import default


def main():

    from collections import defaultdict
    al = list(map(int, input().split()))
    d = defaultdict(int)
    for a in al:
        d[a] += 1
    if len(d) != 2:
        print("No")
        return
    dd = [a for a in d.values()]
    dd.sort()
    if dd[0] == 2 and dd[1] == 3:
        print("Yes")
        return
    print("No")

if __name__ == '__main__':
    main()
