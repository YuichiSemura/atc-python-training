def main():

    n = int(input())
    pl = list(map(int, input().split()))
    
    i = n
    count = 0
    while i != 1:
        i = pl[i-2]
        count+=1
    print(count)

if __name__ == '__main__':
    main()
