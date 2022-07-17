def main():

    l = list(input())
    l.sort()
    if l[0] == l[1] and l[0] == l[2]:
        print(-1)
        return 
    if l[0] == l[1]:
        print(l[2])
        return 
    if l[1] == l[2]:
        print(l[0])
        return
    print(l[0])


if __name__ == '__main__':
    main()
