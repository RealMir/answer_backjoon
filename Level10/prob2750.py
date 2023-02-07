import sys
input = sys.stdin.readline

def buble_sort(a):
    n = len(a)
    for i in range(n-1):
        exchng = 0
        for j in range(n-1,i,-1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
                exchng += 1
        if exchng == 0:
            break

n = int(input())
lst = [None] * n

for i in range(n):
    lst[i] = int(input())

buble_sort(lst)

for i in range(n):
    print(lst[i])