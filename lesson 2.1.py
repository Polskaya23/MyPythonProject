user_input = int(input("type a four digit number: "))
dig1 = user_input // 1000
dig2 = (user_input - (dig1 * 1000)) // 100
dig3 = (user_input - (dig1 * 1000) - (dig2 * 100)) // 10
dig4 = user_input - (dig1 * 1000) - (dig2 * 100) - (dig3 * 10)
print(dig1, dig2, dig3, dig4, sep='\n')