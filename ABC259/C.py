def main():

    s = input()
    t = input()
    
    i = 1
    chb = s[0]
    count = 1
    ls = []
    while i < len(s):
        if chb == s[i]:
            count += 1
        else:
            ls.append((chb, count))
            chb = s[i]
            count = 1
        i+=1
    ls.append((chb, count))
    
    i = 1
    chb = t[0]
    count = 1
    lt = []
    while i < len(t):
        if chb == t[i]:
            count += 1
        else:
            lt.append((chb, count))
            chb = t[i]
            count = 1
        i+=1
    lt.append((chb, count))
    
    if len(ls) != len(lt):
        print("No")
        return
    for (ss, sl), (tt, tl) in zip(ls, lt):
        if ss != tt or sl == 1 and tl != 1 or sl > tl:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()
