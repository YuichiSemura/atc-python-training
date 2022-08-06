def main():

    n, m = map(int, input().split())
    dl = [[str(i+1)] for i in range(m)] # [1, 2, 3].. のdictを作る
    for i in range(n-1):
        ndl = [[] for _ in range(m)]
        for nind, nd in enumerate(ndl):
            for dd in dl[nind+1:]:
                for ddd in dd:
                    nd.append(str(nind+1) + " "+ ddd)
        dl = ndl
    for d in dl:
        for dd in d:
            print(dd)

if __name__ == '__main__':
    main()
