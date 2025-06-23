lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
halfListLen = len(lst) // 2
if len(lst) == 0:
    print([[], []])
elif len(lst) % 2 == 0:
    lst1 = lst[:halfListLen]
    lst2 = lst[halfListLen:]
    print([lst1, lst2])
else:
    lst1 = lst[:halfListLen+1]
    lst2 = lst[halfListLen+1:]
    print([lst1, lst2])


