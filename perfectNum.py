x = int(input("Please enter a number: "))
for i in range(1, x+1):
    if x % i == 0:
        print(i)

def pfct_num(m):
    temp = m
    i = 1
    sum = 0

    while (i < m):
        if m % i == 0:
            sum = sum + i
        i = i + 1

        if (sum == temp):
            print("Is the number a perfect number? True ")
    print("Is the number a perfect number? False ")

num = int(input("Please enter the number again: "))
pfct_num(num)

