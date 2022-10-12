# itertools: product, permutations, combinations, accumulate, groupdby, infinite iterators.
from itertools import product
from itertools import permutations
from itertools import combinations
from itertools import accumulate
from itertools import groupby
# from itertools import infinite iterators 

arr1 = [1, 2]
arr2 = [3, 4]
prod = product(arr1, arr2)
print(list(prod))

arr3 = [1, 2, 3]
perm = permutations(arr3)
print(list(perm))

arr4 = [1, 2, 3, 4]
comb = combinations(arr4, 3)
print(list(comb))

arr5 = [1, 2, 3, 4]
acc = accumulate(arr5)
print(arr5)
print(list(acc))

person = [{'name': 'Tim', 'age':25}, {'name': 'Dan', 'age':25},{'name': 'Lisa', 'age':27},{'name': 'Claire', 'age':28}]
group_obj = groupby(person, key=lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value))