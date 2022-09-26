n = int(input("Please Enter a Number:"))

def sum_odd(n):
    odd = 0
    for number in range(1, n+1):
        if(number % 2 == 1):
            print(number)
            odd = odd + number
    print("The sum of odd numbers are: ", odd)
    
sum_odd(n)
