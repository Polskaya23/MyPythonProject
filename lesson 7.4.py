def common_elements():
    my_range = range(0, 100)
    mult3 = set()
    mult5 = set()
    for x in my_range:
        if x % 3 == 0:
            mult3.add(x)
        if x % 5 == 0:
            mult5.add(x)
    return mult3.intersection(mult5)



assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
