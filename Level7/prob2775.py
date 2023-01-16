t = int(input())
for _ in range(t):
  a = int(input())
  b = int(input())
  lst = [x for x in range(1, b + 1)]

  for _ in range(a):
    result = []
    for i in range(1, b + 1):
      sum = 0
      for j in range(i):
        sum += lst[j]
      result.append(sum)
    lst = result
  print(result[-1])
