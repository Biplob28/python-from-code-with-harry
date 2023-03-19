# find prime number

num = int(input("enter the number:\n"))
prime=True

for i in range(2, num):
    if(num%i == 0):
        prime= False
        break
if prime:
        print("this is prime number\n")
else:
        print("this is not the prime number\n")
    
       