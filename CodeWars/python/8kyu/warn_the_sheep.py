def warn_the_sheep(queue):
    # return queue
    if queue != "sheep":
        return "Pls go away and stop eating my sheep"
    else:
        return f"Oi! Sheep number {queue[0]}! You are about to be eaten by a wolf!"





print(warn_the_sheep("s"))