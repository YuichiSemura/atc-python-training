def main():

    from operator import itemgetter
    n = int(input())
    al = [list(map(int, input().split())) for _ in range(n)]
    al.sort(key=itemgetter(0))
    kl = []
    left = al[0][0]
    right = al[0][1]
    for a in al[1:]:
        if right < a[0]:
            kl.append((left, right))
            left = a[0]
            right = a[1]
            continue
        if right < a[1]:
            right = a[1]
    kl.append((left, right))
    for ka, kb in kl:
        print(ka, kb)

if __name__ == '__main__':
    main()
