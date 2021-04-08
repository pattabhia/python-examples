def show(message, str):
    print(message, str)
    return


def add(mylist):
    mylist.append([3, 4, 5])
    return mylist


show("Greetings", "Hello Abhi")
show("list content is", add([1, 2]))
