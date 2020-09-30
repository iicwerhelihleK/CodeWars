"""
Your task is to create a function isDivideBy (or is_divide_by) to check if an integer number is divisible by each out of two arguments.
"""

def is_divide_by(number, a, b):
    # if number % a == 0 and number % b == 0:
    #     return True
    # else:
    #     return False


    return (number % a == 0 or number % b == 0)



print(is_divide_by(6, 4, 2))