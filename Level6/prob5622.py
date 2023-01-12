s = input()
t = 0
for i in s:
  if i in "ABC": t += 3
  elif i in "DEF": t += 4
  elif i in "GHI": t += 5
  elif i in "JKL": t += 6
  elif i in "MNO": t += 7
  elif i in "PQRS": t += 8
  elif i in "TUV": t += 9
  else: t += 10
print(t)