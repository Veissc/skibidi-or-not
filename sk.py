import sys

sys.setrecursionlimit(10**8)
a = list(map(int, input().split()))
cnt = 0
def f(s,k):
    global cnt
    cnt +=1
    if cnt >= 10**6: return 0
    if s > k: return 0
    if s == k: return 1
    if s <= 0: return f(s+3, k)
    return f(s + 3, k) + f(s + 3, k)
if f(a[0], a[1]) != 0:
    print('YES')
else:
    print('NO')