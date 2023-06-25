def main():

    al = list(map(int, input().split()))
    ans = 0
    for i in range(64):
        ans = ans * 2 + al[63 - i]
    print(ans)

if __name__ == '__main__':
    main()
    
"""

"""