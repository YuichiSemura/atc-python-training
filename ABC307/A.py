def main():

    n = int(input())
    al = list(map(int, input().split()))
    print(" ".join([str(sum(al[i*7:i*7+7])) for i in range(n)]))
        

if __name__ == '__main__':
    main()

"""

"""