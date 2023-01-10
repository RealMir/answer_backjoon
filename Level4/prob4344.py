import sys

input = sys.stdin.readline

c = int(input())
for _ in range(c):
  t = list(map(int, input().split()))
  avg = sum(t[1:]) / t[0]
  cnt = 0
  for score in t[1:]:
    if score > avg:
      cnt += 1
  rate = cnt / t[0] * 100
  print(f"{rate:.3f}%")
