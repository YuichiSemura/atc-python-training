def main():

    n = int(input())
    al = [input() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            s = al[i]+al[j]
            if s == s[::-1]:
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    main()

"""

"""