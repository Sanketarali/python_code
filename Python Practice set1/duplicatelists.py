names=[]
n=int(input("Enter the number\n"))
for i in range(n):
    print(i+1,"Enter the names\n")
    names.append(input())

s=set(names)
names=list(s)
for x in names:
    print(x)    

