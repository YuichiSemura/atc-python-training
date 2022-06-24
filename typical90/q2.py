# 002 - Encyclopedia of Parentheses
def main():

    n = int(input())
    if n % 2 == 1:
        exit(0)

    for i in list(range(2**n+1, 2**(n+1))):
        l = ['(' if b == '0' else ')' for b in bin(i)[3:]]
        count = 0
        for b in l:
            if b == '(':
                count += 1
            else:
                count -= 1
            if count < 0:
                break
        if count == 0:
            print(''.join(l))


if __name__ == '__main__':
    main()
