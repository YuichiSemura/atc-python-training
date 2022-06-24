def main():

    N = int(input())
    cl1 = [0]
    cl2 = [0]
    for _ in range(N):
        ci, pi = map(int, input().split())
        if ci == 1:
            cl1.append(cl1[-1] + pi)
            cl2.append(cl2[-1])
        else:
            cl1.append(cl1[-1])
            cl2.append(cl2[-1] + pi)
    Q = int(input())
    for _ in range(Q):
        li, ri = map(int, input().split())
        print(cl1[ri] - cl1[li - 1], cl2[ri] - cl2[li - 1])


if __name__ == '__main__':
    main()

"""
7
1 72
2 78
2 94
1 23
2 89
1 40
1 75
1
2 6


"""
