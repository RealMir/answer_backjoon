t = int(input())
lst = []
for _ in range(t):
  a, b = map(int, input().split())
  lst.append(a + b)
for i in range(t):
  print(lst[i])
