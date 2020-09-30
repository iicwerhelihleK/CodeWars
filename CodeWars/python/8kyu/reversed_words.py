def reverseWords(s):
    # string = " ".join(s.split()[::-1])
    # return string
    # return " ".join(reversed(s.split()))

    
    # s = ["My ", "name ",  "is ", "Odwa "]
    str_split = s.split()
    string = " "
    for i in str_split:
        string = i + " " + string
    return string.rstrip()



print(reverseWords("hello world! "))
# "awdO si eman yM"

# "Odwa is name My"