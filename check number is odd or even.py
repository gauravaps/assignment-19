# write a python program to create a function to check wheater a given number is even or odd.

'''def check(item):
    if item%2==0:
     print("even number ")
    else:
        print("odd number")

check(7)'''

def check(item):

    for i in item:
    
        if i%2==0:
            
            print("even number is =" ,i)


        else:
            ("odd number")
a=[8,9,4,12]
print(check(a))        