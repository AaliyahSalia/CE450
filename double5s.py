def double_5():
    n = int(input("Please enter a number: "))
    flag = 0
    while n > 0:
        n, m = n // 10, n % 10
        if m == 5 and flag == 1:
            return True
        elif m == 5:
            flag = 1
        else:
            flag = 0
    return False
print(double_5())
