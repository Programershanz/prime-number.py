#program to take out prime numbers
num = int(input("enter a number:"))

isPrime = 1
if (num <0):
    loopRange = -(num)
else:
    loopRange = num

if (num == 1 or num == 0):
    isPrime=0
    print("are neither a composite nor a prime!")

for i in range(2,loopRange):
    print ("{} % {} = {}" .format(num,i,num%i))
    
    # If num is divisible, then modulus operator will return value of 0
    # examle: 4 % 2 = 0
    # example: 5 % 2 = 1
    if (num % i == 0):
        print("{} is Not Prime".format(num))
        isPrime = 0
        #to break to the loop when the number is divisible by any number
        break

if (isPrime == 1):
    print("{} is Prime".format(num))

       

        
