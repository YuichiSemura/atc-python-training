N = int(input())
a = list(map(int,input().split()))
M = 0
ans = [0]*(2*N+1)
flag = True
for i in range(2*N):
    if M > a[i]:
        if ans[M] == -1 or ans[a[i]] == 1:
            flag = False
        ans[M],ans[a[i]] = 1,-1
    else:
        M = a[i]
print(ans)
 
 
b = list(map(int,input().split()))
m = 2*N+1
for i in range(2*N):
    if m < b[i]:
        if ans[m] == -1 or ans[b[i]] == 1:
            flag = False
        ans[m],ans[b[i]] = 1,-1
    else:
        m = b[i]
print(ans)
print(flag)
ans.pop(0)
print(ans)
sa,sb = 0,0
for i in range(2*N):
    sa += ans[a[i]-1]
    sb += ans[b[i]-1]
    print(sa)
    print(sb)
    if sa < 0 or sb < 0 or ans[i] == 0:
        flag = False

if flag:
    d = ["","(",")"]
    ans = [d[v] for v in ans]
    print("".join(ans))
else:
    print(-1)