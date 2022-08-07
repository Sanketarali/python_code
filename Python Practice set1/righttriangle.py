# Python program to interchange first and last elements in a list

l=[1,2,3,4]
# print(l[len(l)-1])
l[0]=l[3]
l[len(l)-1]=l[3]
print(l)