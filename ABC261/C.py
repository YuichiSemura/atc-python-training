def main():

    from collections import defaultdict
    dd = defaultdict(int)
    for _ in range(int(input())):
        s = input()
        if s not in dd:
            print(s)
        else:
            print(f"{s}({str(dd[s])})")
        dd[s] += 1
    
if __name__ == '__main__':
    main()
