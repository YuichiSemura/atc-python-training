def main():

    n, m, t = map(int, input().split())
    al = list(map(int, input().split()))
    
    bonus = [0] * n
    for i in range(m):
        xx, yy = map(int, input().split())
        bonus[xx-1] = yy
    
    count = t
    for ind, a in enumerate(al):
        count -= a
        # print(count)
        if count <= 0:
            print("No")
            return
        count += bonus[ind+1]
        # print("  ", count)
        
    print("Yes")

if __name__ == '__main__':
    main()
