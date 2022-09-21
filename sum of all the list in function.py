# write a python script to sum all the number in a list

from ast import Num


def lst(item):
    sum=0
    for i in item:
        sum=sum+i
    return sum 
Num=[5,8,6,7]           
print(lst(Num))       

