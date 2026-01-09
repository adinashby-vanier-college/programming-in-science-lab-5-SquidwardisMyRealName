# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    result = "*" * n + ("\n*" + " " * (n-2) + "*") * (n-2)
    if n > 1:
        result += "\n" + "*" * n

    return result  

# natural_number = int(input("Enter a natural number: "))
# hollow_square(natural_number)
# print(hollow_square(natural_number))


# 1
# 12
# 123
# 1234
def number_pattern(n):
    result = "" 

    for i in range (1, n + 1):
        for j in range (1, i + 1):
            result += str(j)
        result += "\n"
    
    return result.rstrip()

# n = int(input("Enter a natural number: "))
# print(number_pattern(n)) 

# natural_number = int(input("Enter a natural number: "))
# number_pattern(natural_number)
# print(number_pattern(natural_number))

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    result = 0
    for natural_numbers in range(0, n + 1): 
        result += natural_numbers 
    return result    

# natural_number = int(input("Enter a natural number: "))
# sum_of_natural_numbers(natural_number)
# print(sum_of_natural_numbers(natural_number)) 


# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    result = ""
    i = 1 

    for i in range(n):
        for j in range (n - i - 1):
            result += " "
        for k in range (2 * i + 1):
            result += "*"
        result += "\n"
    return result.rstrip()


# natural_number = int(input("Enter a natural number: "))
# centered_star_pyramid(natural_number)
# print(centered_star_pyramid(natural_number))
