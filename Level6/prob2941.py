# first way
croatia = ["dz=", "c=", "c-", "d-", "lj", "nj", "s=", "z="]
s = input()
idx = cnt = 0
while idx != len(s):
  if s[idx:idx + 3] == croatia[0]:
    idx += 3
  elif s[idx:idx + 2] in croatia:
    idx += 2
  else:
    idx += 1
  cnt += 1
print(cnt)

# second way
croatia = ["dz=", "c=", "c-", "d-", "lj", "nj", "s=", "z="]
s = input()
for i in croatia:
  s = s.replace(i, "*")
print(len(s))