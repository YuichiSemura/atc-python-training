def main():

    n = int(input())
    st = set()
    for i in range(n):
        s = input()
        if s in st:
            continue
        st.add(s)
        print(i+1)

if __name__ == '__main__':
    main()

"""

"""