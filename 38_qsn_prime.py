number=int(input("Enter a number:"))
for i in range(2,number):
    if(number%i==0):
        print("%d is not prime number."%number)
        break
else:
    print("%d is a prime number."%number)