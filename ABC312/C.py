def main():

    n, m = map(int, input().split())
    al = list(map(int, input().split()))
    bl = list(map(int, input().split()))
    print(sorted(al + list(map(lambda x: x + 1, bl)))[m - 1])


if __name__ == '__main__':
    main()

"""

"""