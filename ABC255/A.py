def main():

    n, m = map(int, input().split())
    al = list(map(int, input().split()))
    bl = list(map(int, input().split()))
    al = [al, bl]
    print(al[n-1][m-1])

if __name__ == '__main__':
    main()
