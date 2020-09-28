def hello(name= ""):
    # answer = (f"Hello, {name or 'world'}!".title())
    # # answer = "Hello, " + (name.capitalize() or "World") + "!"
    # print(answer)

    if name == "":
        return "Hello, World!"
    else:
        return "Hello, " + name.capitalize() + "!"


print(hello("Odwa"))
