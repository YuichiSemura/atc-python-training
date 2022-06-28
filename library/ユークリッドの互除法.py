def main():

    n, m = map(int, input().split())
    print(euclidean(n, m))

def euclidean(n: int, m: int):
    
    while True:
        n = n % m
        if n == 0:
            return m
        m, n = n, m

if __name__ == '__main__':
    main()
