# 5.Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

prime = list()
for i in range(1,100):
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            prime = prime + [i]
                
print(f"Prime = {prime}")


    
