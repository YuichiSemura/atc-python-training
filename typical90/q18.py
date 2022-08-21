import math

def main():

    T = int(input())
    L, X, Y = map(int, input().split())
    Q = int(input())
    xx = X ** 2
    for _ in range(Q):
        e = int(input())
        rad = ( e % T ) / T * math.pi * 2
        yt = - L / 2 * math.sin(rad)
        zt = L / 2 * (1 - math.cos(rad))
        yy = xx + (yt - Y) ** 2
        zz = yy + zt ** 2
        print(math.degrees(math.acos(math.sqrt(yy) / math.sqrt(zz))))

if __name__ == '__main__':
    main()
