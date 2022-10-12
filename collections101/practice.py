# coolections: Counter, namedtuple, OrderdDict, defaultdict, deque

from collections import Counter
var1 = "aaaaaabbbbbbbbbcccccdddddd"
my_counter = Counter(var1)
print(my_counter)
print(my_counter.most_common(1))