lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if len(lst) > 1:
    last = lst[-1]
    lst.pop()
    lst.insert(0, last)
print(lst)

