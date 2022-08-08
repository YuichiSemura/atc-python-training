def main():

    n = int(input())
    cl = list(map(int, input().split()))
    xl = list(map(int, input().split()))
    al = [[c, x] for c, x in zip(cl, xl)]

    count = 0
    for i in range(n-1):
        for j in range(n-1):
            if al[j][1] > al[j + 1][1]:
                if al[j][0] != al[i][0]:
                    count+=1
                tmp = al[j]
                al[j] = al[j + 1]
                al[j + 1] = tmp
    print(count)

if __name__ == '__main__':
    main()

