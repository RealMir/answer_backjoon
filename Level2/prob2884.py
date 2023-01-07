h, m = map(int, input().split())
m -= 45
if m < 0:
  h -= 1
print(h % 24, m % 60)
