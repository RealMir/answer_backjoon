n = int(input())
num = n // 5
rest = n % 5

if rest == 0:
  print(num)
else:
  for i in range(num, -1, -1):
    if rest % 3 == 0:
      print(i + rest // 3)
      break
    rest += 5
  else:
    print(-1)