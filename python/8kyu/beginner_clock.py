def past(hours, minutes, seconds):
    # millis=input("Enter time in milliseconds ")
    millis = int(millis)
    seconds=(millis/1000)%60
    seconds = int(seconds)
    minutes=(millis/(1000*60))%60
    minutes = int(minutes)
    hours=(millis/(1000*60*60))%24

    return ((hours, minutes, seconds))



if __name__ == '__main__':
    print(past(0, 1, 1))
    