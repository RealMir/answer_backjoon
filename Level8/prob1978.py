n = int(input())
x = list(map(int, input().split()))

cnt = 0
for i in range(n):
  if x[i] == 1:
    continue
  else:
    for j in range(2, x[i]):
      if x[i] % j == 0:
        break
    else:
      cnt += 1
print(cnt)