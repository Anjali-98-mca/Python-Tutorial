"""From a list of integers, create a list removing even numbers."""
list_1=[-5,-4,-3,-2,-1,0,1,2,3,4,5,6]
print(list_1)
print([x for x in list_1 if x%2!=0])

for x in list_1:
    if x%2==0:
        list_1.remove(x)

print(list_1)