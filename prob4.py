# 4.	Write a Python Program to Check Prime Number?

n = int(input("Enter the number you want to check : "))
prime = True
for i in range(2,n):
    if n % i == 0:
        prime = False
        break
if prime :
    print("The given number is prime ")
else:
    print("The given number is not prime ")