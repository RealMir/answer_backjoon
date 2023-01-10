import sys

input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
maxium = max(lst)
sum = sum(lst)
print(sum / maxium * 100 / n)
