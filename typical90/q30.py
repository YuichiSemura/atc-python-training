# 素数

def main():

    n, k = map(int, input().split())
    counter = [0] * (n + 1)
    counter[1] = 1
    for i in range(2, n+1):
        if counter[i] != 0:
            continue
        for j in range(i, n+1, i):
            counter[j] += 1
    print(len([c for c in counter[2:] if c >= k]))

if __name__ == '__main__':
    main()

"""
10000000 3

"""