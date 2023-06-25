def checkA(ha, wa, al, ai, aj, cl, seen) -> bool:

    for aai in range(ha):
        for aaj in range(wa):
            if al[aai][aaj]:
                if not cl[ai + aai][aj + aaj]:
                    return False
                else:
                    seen[ai + aai][aj + aaj] = True
    return True

def checkB(hb, wb, bl, bi, bj, cl, seen) -> bool:

    for bbi in range(hb):
        for bbj in range(wb):
            if bl[bbi][bbj]:
                if not cl[bi + bbi][bj + bbj]:
                    return False
                else:
                    seen[bi + bbi][bj + bbj] = True
    return True

def checkSeen(cl, seen):
    
    for xi in range(29):
        for xj in range(29):
            if cl[xi][xj] != seen[xi][xj]:
                return False
    return True

def main():

    ha, wa = map(int, input().split())
    al = [[True if s == '#' else False for s in input()] for _ in range(ha)]

    hb, wb = map(int, input().split())
    bl = [[True if s == '#' else False for s in input()] for _ in range(hb)]

    hx, wx = map(int, input().split())
    xl = [[True if s == '#' else False for s in input()] for _ in range(hx)]
    for ai in range(0, 19):
        for aj in range(0, 19):
            for bi in range(0, 19):
                for bj in range(0, 19):
                    # 空の配列を作る
                    cl = [[False] * 29 for _ in range(29)]
                    # チェック用の配列を作る
                    seen = [[False] * 29 for _ in range(29)]
                    # X を C にコピーする
                    for xi in range(hx):
                        for xj in range(wx):
                            cl[9+xi][9+xj] = xl[xi][xj]
                    # AのすべてがCに含まれていることをチェックし、seenにもcheckする
                    if not checkA(ha, wa, al, ai, aj, cl, seen):
                        continue
                    # BのすべてがCに含まれていることをチェックし、seenにもcheckする
                    if not checkB(hb, wb, bl, bi, bj, cl, seen):
                        continue
                    # チェックしたことで全て埋まっていることを確認する
                    if not checkSeen(cl, seen):
                        continue
                    print("Yes")
                    return
    print("No")


if __name__ == '__main__':
    main()
