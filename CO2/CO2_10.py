"""Generate all factors of a number."""

num=int(input("Enter a number="))

print("the factors of the number=")
for x in range(1,num+1):
    if num%x==0:
        print(x," ",end="")