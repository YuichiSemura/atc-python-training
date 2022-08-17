def main():

    r, c = map(int, input().split())
    print("black" if min(r, 16-r, 16-c, c) % 2 == 1 else "white")

if __name__ == '__main__':
    main()
