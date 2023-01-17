m = int(input())
n = int(input())

x = [i for i in range(m, n + 1)]
result = []

for i in range(len(x)):
  if x[i] == 1:
    continue
  else:
    for j in range(2, x[i]):
      if x[i] % j == 0:
        break
    else:
      result.append(x[i])

if len(result) > 0:
  print(f"{sum(result)}\n{result[0]}")
else:
  print(-1)
