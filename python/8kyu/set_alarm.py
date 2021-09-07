def alarm(employed, vacation):
    if employed == True:
        return True
    elif vacation == True:
        return False



if __name__ == '__main__':
    print(alarm(True, False))
    