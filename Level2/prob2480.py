a, b, c = map(int, input().split())
if a == b == c:
  print(10000 + 1000 * a)
elif a != b and a != c and b != c:
  if a < b: a = b
  if a < c: a = c
  print(100 * a)
else:
  if b == c: a = b
  print(1000 + 100 * a)
