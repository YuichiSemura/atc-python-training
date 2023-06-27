# 未完成

def main():

    from collections import defaultdict
    n, m = map(int, input().split())
    abl = [map(int, input().split()) for _ in range(m)] 
    v = [defaultdict(int) for _ in range(n)]
    
    
    for a, b in abl:
        v[a-1][str(b-1)] += 1
    print(v)
    result = 0
    for x, dic in enumerate(v):
        for y, count in dic.items():
            print(x, y, count, v[int(y)][str(x)])
            result += count * v[int(y)][str(x)]
    print(result)

if __name__ == '__main__':
    main()
