list1=[12,63,8,4,18]
list2=[6,14,58,71,40]

print(list1)
print(list2)

if len(list1)==len(list2):
    print("list are of same length")
else:
    print("List are not of same length")


if sum(list1)==sum(list2):
    print("List are of same sum")
else:
    print("List are not of same sum")

list3=[x for x in list1 if x in list2]
if len(list3)<1:
    print("No value occure in both")
else:
    print("common values:",list3)