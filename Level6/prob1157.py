s = input()
s = s.upper()
maxium = x = 0
for i in range(65, 91):
  cnt = s.count(chr(i))
  if cnt > maxium:
    maxium = cnt
    x = i
  elif maxium == cnt:
    x = 63
print(chr(x))