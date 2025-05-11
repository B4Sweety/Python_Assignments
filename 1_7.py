def is_divisible_by_5(number):
    
    if number % 5 == 0:
        return True
    else:
        return False

num = int(input("Enter a number: "))

result = is_divisible_by_5(num)
print(result)
