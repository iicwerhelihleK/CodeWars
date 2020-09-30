import math

def get_average(marks):
    try:
        total = 0
        # marks = [15, 18, 2, 36, 12, 78, 5, 6, 9]
        for i in marks:
            total += i

        mean = math.floor(total / len(marks))
        return mean
    except:
        raise NotImplementedError("TODO: get_average")

   

    




print(get_average([15, 18, 2, 36, 12, 78, 5, 6, 9]))