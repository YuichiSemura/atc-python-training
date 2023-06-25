def main():

    n = int(input())
    al = list(map(int, input().split()))
    sl = [[] for _ in range(n)]
    for ind, a in enumerate(al):
        sl[a-1].append(ind+1)
    sll = [(ind, s[1]) for ind, s in enumerate(sl)]
    sll2 = sorted(sll, key=lambda x: x[1])
    print(' '.join([str(s[0]+1) for s in sll2]))


if __name__ == '__main__':
    main()
    
"""

"""