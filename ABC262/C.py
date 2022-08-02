def main():

    n = int(input())
    al = list(map(int, input().split()))
    cl = []
    count = 0
    for i in range(n):
        al[i] -= 1
        if al[i] == i:
            cl.append(i)
    count += len(cl) * (len(cl)-1) // 2
    for i in range(n):
        if i < al[i] and al[al[i]] == i:
            count += 1
    print(count)


if __name__ == '__main__':
    main()
