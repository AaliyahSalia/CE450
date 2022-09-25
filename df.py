def df(x=0, y=0, z=0):
    x = int(input("Please enter a number: "))
    y = int(input("Please enter a number: "))
    z = int(input("Please enter a number: "))
    
    if (x - y == z or y - x == z):
        print(True)
    else:
        print(False)

df()
