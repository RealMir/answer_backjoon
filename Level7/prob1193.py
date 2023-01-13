n = int(input())
sum = i = 0
while n > sum:
  i += 1
  sum += i
idx = sum - n
print(f"{i-idx}/{1+idx}" if i % 2 == 0 else f"{1+idx}/{i-idx}")