# write a python program to create a function program that finds a maximum of four numbers..

'''def max(a,b):
    if a>b:
        return a
    else:
        return b
a=5
b=6
print(max(a,b))  '''

def maxi(a,b,c,d):
    if a>b and a>c:
        largest=a
    elif b>a and b>c:
        largest=b
    elif d>a and d>b:
        largest=d
    else:
        largest=c
    return largest

a,b,c,d=11,12,13,14
print(maxi(a,b,c,d))                 


    