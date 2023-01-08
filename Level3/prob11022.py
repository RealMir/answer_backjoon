import sys

input = sys.stdin.readline

t = int(input())
for i in range(1, 1 + t):
  a, b = map(int, input().split())
  print(f"Case #{i}: {a} + {b} = {a+b}")
