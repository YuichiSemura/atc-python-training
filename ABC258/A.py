def main():

    n = int(input())
    print(f"{21+(n//60)}:{format(n%60, '02')}")
    
if __name__ == '__main__':
    main()
