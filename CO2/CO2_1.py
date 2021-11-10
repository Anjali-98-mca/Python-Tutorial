"""Program to find the factorial of a number"""
num=int(input("enter a number="))
fact=1

for x in range(1,num+1):
    fact=fact*x
print("factorial=",fact)

fact=1
while num>0:
    fact=fact*num
    num-=1
print("factorial=",fact)