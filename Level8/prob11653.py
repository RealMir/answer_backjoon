n = int(input())

while n % 2 == 0:
  print(2)
  n //= 2

for i in range(3, n + 1, 2):
  if n == 1: break
  while n % i == 0:
    print(i)
    n //= i
