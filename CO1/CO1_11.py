"""Find biggest of 3 numbers entered."""

num1,num2,num3=[int(x) for x in input("enter 3 numbers=").split()]
print("Biggest number=",max(num1,num2,num3))


list1=[num1,num2,num3]
list1.sort()
print("Biggest number=",list1[-1])