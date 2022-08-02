def main():

    n, m = map(int, input().split())
    gl = [set() for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        gl[u-1].add(v-1)
    
    count = 0
    for i in range(n):
        for j in gl[i]:
            count += len(gl[i] & gl[j])
    print(count)

if __name__ == '__main__':
    main()
