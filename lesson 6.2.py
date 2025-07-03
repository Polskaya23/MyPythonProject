user_input = int(input("Enter the number of seconds: "))
if 0 <= user_input < 8640000:
    days, remaining = divmod(user_input, 86400)
    hours, remaining = divmod(remaining, 3600)
    minutes, seconds = divmod(remaining, 60)

    if days % 10 == 1 and days % 100 != 11:
        day_word = "день"
    elif days % 10 in [2, 3, 4] and days % 100 not in [12, 13, 14]:
        day_word = "дні"
    else:
        day_word = "днів"
    hours_str = str(hours).zfill(2)
    minutes_str = str(minutes).zfill(2)
    seconds_str = str(seconds).zfill(2)
    print(f"{days} {day_word}, {hours_str}:{minutes_str}:{seconds_str}")
else:
    print("An error: the number must be from 0 up to 8639999")

