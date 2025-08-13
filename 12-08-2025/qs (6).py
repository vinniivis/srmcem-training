def divisible_by_3_or_5_not_both(start=1, end=100):
    for num in range(start, end + 1):
        if (num % 3 == 0) ^ (num % 5 == 0):  
            print(num, end=" ")
divisible_by_3_or_5_not_both(1, 15)
