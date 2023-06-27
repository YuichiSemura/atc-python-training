def main():

    n, k = map(int, input().split())
    al = list(map(int, input().split()))
    bl = list(map(int, input().split()))
    
    s = sum([abs(a - b) for a, b in zip(al, bl)])
    print("Yes" if k >= s and abs(k - s) % 2 == 0 else "No")
        

if __name__ == '__main__':
    main()

"""

"""