n = int(input())

original = n
cnt = 0

while 1:
  cnt += 1
  a = n // 10
  b = n % 10
  n = b * 10 + (a + b) % 10
  if n == original:
    break

print(cnt)