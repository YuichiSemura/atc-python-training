def main():

    n = int(input())
    s = input()
    af = False
    bf = False
    cf = False
    for i in range(n):
        if s[i] == 'A':
            af = True
        elif s[i] == 'B':
            bf = True
        elif s[i] == 'C':
            cf = True
        if af and bf and cf:
            print(i+1)
            break

if __name__ == '__main__':
    main()

"""

"""