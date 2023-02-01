import sys
input = sys.stdin.readline

n,m = map(int, input().split())
a = [None] * n
b = [None] * n

for i in range(n):
    a[i] = list(map(int, input().split()))

for i in range(n):
    b[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(m):
        print(a[i][j]+b[i][j], end=" ")
    print()