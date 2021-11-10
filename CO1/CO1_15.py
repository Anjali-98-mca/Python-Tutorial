"""Print out all colors from color-list1 not contained in color-list2."""

colorlist_1=["yellow","pink","blue","indigo","black"]
colorlist_2=["violet","black","orange","green","yellow"]

print(colorlist_1)
print(colorlist_2)
print("all colors from color-list1 not contained in color-list2")
print([x for x in colorlist_1 if x not in colorlist_2])

set_1=set(colorlist_1)
set_2=set(colorlist_2)
set_3=set_1.difference(set_2)
print("all colors from color-list1 not contained in color-list2")
print(list(set_3))