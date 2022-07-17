def main():

    n, x, y = map(int, input().split())
    red, blue = 1, 0
    for i in range(n, 1, -1):
        red, blue = red, x * red + blue
        red, blue = red + blue, blue * y
    print(blue)

if __name__ == '__main__':
    main()
