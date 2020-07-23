import random
list_size = 15
min_in_list = 0
max_in_list = 1000
start_list = [random.randrange(min_in_list,max_in_list) for i in range(0, list_size)]
print(f"start_list {start_list}")
finish_list = [start_list[i] for i in range(1, len(start_list)) if start_list[i] > start_list[i-1]]
print(f"finish_list {finish_list}")