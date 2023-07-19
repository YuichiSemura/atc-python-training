def main():

    n = int(input())
    s = list(input())
    
    one, zero = 0, 0
    countl = [one]
    for ss in s:
        if ss == "0":
            one, zero = one + zero, 1
        else:
            one, zero = zero + 1, one
        countl.append(one)
    print(sum(countl))
if __name__ == '__main__':
    main()

"""

"""