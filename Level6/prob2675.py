import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
  a, b = input().split()
  for i in b:
    print(i * int(a), end="")
  print()
