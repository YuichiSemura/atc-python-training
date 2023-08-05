def main():

    n = int(input())
    al = list(map(int, input().split()))
    al.sort()
    sm = sum(al)
    bl = [sm // n for i in range(0, n)]
    q = sm // n
    for i in range(0, sm % n):
        bl[n - 1 - i] += 1
    print(sum([abs(al[i] - bl[i]) for i in range(n)]) // 2)

if __name__ == '__main__':
    main()

"""

"""