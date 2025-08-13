def sum_of_digits(num):
    total = 0
    for digit in str(abs(num)):
        total += int(digit)
    return total
print(sum_of_digits(12345))
