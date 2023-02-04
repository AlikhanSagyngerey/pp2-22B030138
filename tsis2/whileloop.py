i = 1
while i < 6:
  print(i)
  i += 1

b = 1
while b < 6:
  print(b)
  if b == 3:
    break
  b += 1

c = 0
while c < 6:
  c += 1
  if c == 3:
    continue
  print(c)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")