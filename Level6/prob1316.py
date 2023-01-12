n = int(input())
result = n
for _ in range(n):
  s = input()

  for i in range(97, 123):
    i = chr(i)
    if i in s:
      if s.rfind(i) - s.find(i) + 1 != s.count(i):
        result -= 1
        break
print(result)