def expression_out(exp):
    operators = { 
      '+':   'Plus ',
      '-':   'Minus ',
      '*':   'Times ',
      '/':   'Divided By ',  
      '**':  'To The Power Of ',
      '=':   'Equals ',
      '!=':  'Does Not Equal ' 
    }
    numbers = {
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine",
        "10": "Ten"
    }

    invalid_operator  = "This is not an operator"

    new_list = exp.split()
    print(new_list)


    # new_str = ""
    # # print(new_list)
    # # print(exp)
    # for i in new_list:
    #     if i == numbers.keys():
    #         new_str += numbers.items()
    #     elif i == operators.keys():
    #         new_str += operators.items()
    # # print(numbers.items())
    # print(numbers.keys())
    # print(new_str)
    # # print(operators.items())
    # print(operators.keys())
    # return exp



print(expression_out(""))
# print("One Plus Two")