def lrgst_factor(n):
    i = n-1
    while i >= 1:
        if n%i==0:
            return i
        i -= 1

n = int(input("Please enter a number: "))
print("The largest factor of the number is: ", lrgst_factor(n))
