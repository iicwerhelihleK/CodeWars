import numpy as np
from operator import add 


"""
- Create a func called sum_arrays()
- Takes in twon arrays consisiting of integers
- Returns the sum of the two arrays
- If both arrays are empty, return an empty array
- If firdt index of the array is a negative number then the whole array is treated as negative
"""

def sum_arrays(array1, array2):
    # count = 0
    # for num in array2, array2:
    #     if num < 0:
    #         count += 1
    #     result = list(map(add, array1, array2))
    # return result
    array1 = np.array(array1)
    array2 = np.array(array2)

    res = array1 + array2





if __name__ == "__main__":
    test_list1 = [1, 3, 4, 6, 8]
    test_list2 = [4, 5, 6, 2, 10] 
    print(sum_arrays(test_list1, test_list2))
