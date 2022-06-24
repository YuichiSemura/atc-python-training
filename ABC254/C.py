def main():

    n, k = map(int, input().split())
    al = list(map(int, input().split()))
    
    for i in range(k):
        al[i::k] = sorted(al[i::k])

    for i in range(1, n):
        if al[i] < al[i-1]:
            print("No")
            exit()
    print("Yes")
    
if __name__ == '__main__':
    main()