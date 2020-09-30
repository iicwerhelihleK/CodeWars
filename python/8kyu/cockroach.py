import unittest
import math
"""
The cockroach is one of the fastest insects. 
Write a function which takes its speed in km per hour and returns it in cm per second, rounded down to the integer (= floored).

"""

def cockroach_speed(s):
    # Good Luck!
    num = math.floor(s)
    return (num)


print(cockroach_speed(1.08))
# cockroach_speed(22.23)



# class TestCockroach(unittest.TestCase): 
#     def test(self):
#         self.assertEquals(cockroach_speed(-2), 20)
    # Test.assertEquals(cockroach_speed(0), False)
    # Test.assertEquals(cockroach_speed(1), True)
    # Test.assertEquals(cockroach_speed(3), True)