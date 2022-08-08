def main():

    n = int(input())
    al = [list(input()) for _ in range(n)]
    
    for i in range(n):
        for j in range(i+1, n):
            if not (al[i][j] == 'W' and al[j][i] == 'L' or al[i][j] == 'L' and al[j][i] == 'W' or al[i][j] == 'D' and al[j][i] == 'D'):
                print("incorrect")
                return
    print("correct")

if __name__ == '__main__':
    main()
