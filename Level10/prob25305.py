import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))

left = 0
right = n-1
last = right

while left < right:
    for i in range(right,left,-1):
        if lst[i] > lst[i-1]:
            lst[i], lst[i-1] = lst[i-1], lst[i]
            last = i
    left = last

    for i in range(left,right):
        if lst[i] < lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
            last = i
    right = last

print(lst[k-1])