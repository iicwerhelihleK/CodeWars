"""
Given an array of ones and zeroes, convert the equivalent binary value to an integer.

Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

However, the arrays can have varying lengths, not just limited to 4.
"""

def binary_array_to_number(arr): 
    # result = int("".join(str(i) for i in arr), 2)
    result = 0
    for i in arr:
        result = result * 2 + i 
        print(i)
    print("The value is: " + str(result))
    return result

    


if __name__ == "__main__":
    the_arr = [0, 1, 0, 1, 0, 1]
    # print("The array is: " + str(the_arr))
    print(binary_array_to_number(the_arr))