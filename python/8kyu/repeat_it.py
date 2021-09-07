"""
Create a function that takes a string and an integer (n).

The function should return a string that repeats the input string n number of times.

If anything other than a string is passed in you should return "Not a string"
"""

def repeat_it(myStr, n):
    if (type(myStr) != str):
        return "Not a string"
    return str(myStr) * n
    



if __name__ == "__main__":
    print("No string: " + str(repeat_it("", 2)))
    print("Empty list: " +str(repeat_it([], 1)))
    print("Repeat name: " + str(repeat_it("Odwa", 3)))

