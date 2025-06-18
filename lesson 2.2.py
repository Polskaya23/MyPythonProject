user_input = int(input("type a five digit number: "))
dig1 = user_input // 10000
dig2 = (user_input - (dig1 * 10000)) // 1000
dig3 = (user_input - (dig1 * 10000) - (dig2 * 1000)) // 100
dig4 = (user_input - (dig1 * 10000) - (dig2 * 1000) -(dig3 * 100)) // 10
dig5 = user_input - (dig1 * 10000) - (dig2 * 1000) - (dig3 * 100) - (dig4 * 10)
print(dig5 * 10000 +  dig4 * 1000 + dig3 * 100 + dig2 * 10 + dig1)