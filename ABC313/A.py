def main():

    n = int(input())
    pl = list(map(int, input().split()))
    if len(pl) == 1:
        print(0)
    else:
        print(max(max(pl[1:])+1 - pl[0], 0 ))

if __name__ == '__main__':
    main()

"""

"""