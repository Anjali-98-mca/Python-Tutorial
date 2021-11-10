"""Create a list of colors from comma-separated color names entered by user. Display
first and last colors."""

cname=input("enter the color names separated by comma=")
l1=cname.split(",")
print("first color=",l1[0])
print("last color=",l1[-1])