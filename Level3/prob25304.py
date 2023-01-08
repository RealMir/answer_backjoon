price = int(input())
num = int(input())
result = 0

for _ in range(num):
  p, n = map(int, input().split())
  result += p * n

print("Yes" if price == result else "No")