myset = {"apple", "banana", "cherry"}
thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset = {"apple", "banana", "cherry"}

print(len(thisset))
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}
myset = {"apple", "banana", "cherry"}
print(type(myset))
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

thisset = {"apple", "banana", "cherry"}

x = thisset.pop() #removes random item

print(x)

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)#keeps the items both in x and y

print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)#keeps items that do not repeat

print(x)

