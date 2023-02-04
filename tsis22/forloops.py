fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for z in "banana":
  print(z)

fruits = ["apple", "banana", "cherry"]
for y in fruits:
  print(y)
  if y == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for d in fruits:
  if d == "banana":
    break
  print(d)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

for x in range(6):
  print(x) #range(6) is not the values of 0 to 6, but the values 0 to 5

for q in range(2, 6):
  print(q)  #values from 2 to 6 (but not including 6)

for e in range(2, 30, 3):
  print(e)  #Increment the sequence with 3

for X in range(6):
  print(X)
else:
  print("Finally finished!")

for Y in range(6):
  if Y == 3: break
  print(Y)
else:
  print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for g in adj:
  for h in fruits:
    print(g, h)

for x in [0, 1, 2]:
  pass