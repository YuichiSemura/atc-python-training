"""
未完
"""

def main():

    n, b, k = map(int, input().split())
    cl = list(map(int, input().split()))
    
    print(cl)
    
    count = 0
    for ai in cl:
        for bi in cl:
            for ci in cl:
                for di in cl:
                    for ei in cl:
                        x = ai * 10000 + bi * 1000 + ci * 100 + di * 10 + ei
                        if x % 7 == 0:
                            count+=1
                            print(x)
    print(count)

if __name__ == '__main__':
    main()

"""
5 2 3
1 4 9
"""