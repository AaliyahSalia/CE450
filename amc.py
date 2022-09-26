def amc(): 
    for x in range(284):
        sum1=1
        sum2=1
        for j in range(2,x):
            if x % j == 0:
                sum1+=j
        for i in range(2,sum1):
                
            if sum1%i == 0:
                sum2+=i
        
        if x==sum2:
            print(x,sum1)
        else:
            pass

if __name__ == "__main__":
    r=amc()
    
