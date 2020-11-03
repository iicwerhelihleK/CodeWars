"""
Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

For example:

summation(8) -> 36
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8

"""
def summation(num):
    # summation = sum(range(num + 1))
    # return summation
    summation = 0
    for i in range(num + 1):
        print(i)
        summation += i
        
    return summation




if __name__ == "__main__":
    print(summation(8))



