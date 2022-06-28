def main():

    n = int(input())
    al = list(map(int, input().split()))
    bl = list(map(int, input().split()))
    count = 0
    al.sort()
    bl.sort()
    for a, b in zip(al, bl):
        count += abs(a-b)
    print(count)

if __name__ == '__main__':
    main()
