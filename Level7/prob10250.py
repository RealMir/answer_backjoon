t = int(input())

for _ in range(t):
  h, w, n = map(int, input().split())
  room = n // h
  floor = n % h
  if floor == 0:
    print(f"{h*100+room}")
  else:
    print(f"{floor*100+room+1}")