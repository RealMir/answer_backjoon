import sys

m, n = map(int, sys.stdin.readline().split())

if m <= 2:
  print(2)
  m = 3

if m % 2 == 0: m += 1

for i in range(m, n + 1, 2):
  j = 3
  while j * j <= i:
    if i % j == 0:
      break
    j += 2
  else:
    print(i)