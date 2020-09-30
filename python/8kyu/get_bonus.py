"""
Build a function that takes in two arguments (salary, bonus). Salary will be an integer, and bonus a boolean.

If bonus is true, the salary should be multiplied by 10. If bonus is false, the fatcat did not make enough money and must receive only his stated salary.

Return the total figure the individual will receive as a string prefixed with "$" for Python
"""

def bonus_time(salary, bonus):
    if bonus == True:
        return "$" + str(salary * 10)
    return "$" + str(salary)



if __name__ == "__main__":
    print(bonus_time(10, 20))







