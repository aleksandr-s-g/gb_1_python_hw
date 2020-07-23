import random
from itertools import groupby
list_size = 30
min_in_list = 0
max_in_list = 3
start_list = [random.randrange(min_in_list,max_in_list) for i in range(0, list_size)]
print(start_list)
noDupes = []
[noDupes.append(i) for i in start_list if i not in noDupes]
print(noDupes)