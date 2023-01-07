a, b = map(int, input().split())
c = int(input())

b += c
if b >= 60:
  a += b // 60

print(a % 24, b % 60)
