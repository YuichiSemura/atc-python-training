def main():

    n, p, q = map(int, input().split())
    dl = list(map(int, input().split()))
    print(min(p, q + min(dl)))

if __name__ == '__main__':
    main()

"""

"""