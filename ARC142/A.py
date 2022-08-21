def main():
    
    n, k = map(int, input().split())
    if k % 10 == 0:
        print(0)
        return
    rk = int("".join(str(k)[::-1]))
    if rk < k:
        print(0)
        return
    kk = k
    ll = set()
    while n >= kk:
        ll.add(kk)
        kk *= 10

    while n >= rk:
        ll.add(rk)
        rk *= 10
    
    print(len(ll))
    
if __name__ == '__main__':
    main()
