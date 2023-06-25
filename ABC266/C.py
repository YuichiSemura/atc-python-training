def main():

    al = [list(map(int, input().split())) for _ in range(4)]
    for i in range(3):
        for j in range(i+1, 4):
            if al[i][0] == al[j][0] and al[i][1] == al[j][1]:
                return False
    return True


def checkAC(x, y):


def checkBD(x, y):

def sgn(x):  # x の符号が正なら 1、負なら -1、0 なら 0 を返す
    if x == 0:
        return 0
    return x // abs(x)

if __name__ == '__main__':
    print("Yes" if main() else "No")

