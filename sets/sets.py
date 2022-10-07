myset = {1, 2, 3, 4}
print(myset)

# a set has no order and will not have duplicate. 
newset = set("Hello")
print(newset)

# set itaration
for i in newset:
    print(i)

# check if value is in set
if 2 in myset:
    print("Yes")
else:
    print("No")

odds = {1, 3, 5, 7, 9}
even = {2, 4, 6, 8}
prime = {1, 2, 3, 5, 7}

u = odds.union(even)
print(u)

i = even.intersection(prime)
print(i)