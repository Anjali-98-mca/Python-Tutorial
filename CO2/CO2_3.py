"""Find the sum of all items in a list"""
li=input("enter the numbers separated with commas=")
li1=li.split(",")

s=0
print("list elements are...")
print(li1)

for x in li1:
    s=s+int(x)
print("sum of all items in a list=",s)

list = [42,25,120,87,55]
print("another list=",list)
print("Sum of List : "+ str(sum(list)))
