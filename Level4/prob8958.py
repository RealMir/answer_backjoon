import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
  s = input()
  result = score = 0
  for i in s:
    if i == "O":
      score += 1
      result += score
    else:
      score = 0
  print(result)
