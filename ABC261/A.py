def main():
    l1, r1, l2, r2 = map(int, input().split())
    if l1 < r2 and r1 < l2 or l2 < r1 and r2 < l1:
        print("0")
        return
    print(min(r1, r2) - max(l1, l2))


if __name__ == '__main__':
    main()
