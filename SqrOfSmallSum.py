import math 

def sum_sqr():
    a = int(input("Please enter a number: "))
    b = int(input("Please enter a number: "))
    c = int(input("Please enter a number: "))
    d = int(input("Please enter a number: "))

    if (a < b and b < c):
        print(a**2 + b**2)
    elif (c < d and d < a):
        print(c**2 + d**2)
    else:
        print(a**2 + d**2)

sum_sqr()
    
        
