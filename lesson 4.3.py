import random
list_len = random.randint(3,10)
lst = []
for x in range(list_len):
  lst.insert(x,random.randint(1,10))
print(lst)
new_lst = [lst[0], lst[2], lst[-2]]
print(new_lst)
