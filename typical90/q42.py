def main():

    k = int(input())
    if k % 9 != 0:
        print(0)
        return
    mod = 10 ** 9 + 7
    ansl = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    for i in range(9, k):
        ansl.append(sum(ansl[i-9:i]) % mod)
    print(ansl[-1])

if __name__ == '__main__':
    main()

"""

"""