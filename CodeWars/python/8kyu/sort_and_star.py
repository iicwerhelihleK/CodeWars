"""
You will be given a vector of strings. You must sort it alphabetically (case-sensitive, and based on the ASCII values of the chars) and then return the first value.

The returned value must be a string, and have "***" between each of its letters.

You should not remove or add elements from/to the array.
"""

def two_sort(array):
    # pre_sorted_arr = sorted(array[0], reverse=False)
    # final_sorted = "***".join(pre_sorted_arr)
    # print(pre_sorted_arr)
    # print(final_sorted)
    for word in array:
        word = array.sort()
        # pre_sorted = array.sort()
        final_sorted = "***".join(word)
    return final_sorted





print(two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]))