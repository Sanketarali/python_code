# import math

# print(math.factorial())
# math.factorial

# another method
factorial=1
num=int(input("Enter the number\n"))
if num<0:
    print("The facorial does not exits")

elif num>0:
    for i in range(1,num+1):
       factorial=factorial*i
       print("The factorial f a number is ",factorial)



# using recursion approach


