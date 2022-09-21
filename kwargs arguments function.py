# write a python program to create a function which expects kwargs arguments.
def add(** kwargs):
    for i in kwargs.items():
        print(i)


lst = {"gaurav":98,"saurav":87,"mohit":88,'roshan':55}


add(**lst)
print(type(lst))
