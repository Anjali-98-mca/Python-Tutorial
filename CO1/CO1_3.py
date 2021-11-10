number_1=[-4,-3,-2,-1,1,2,3,4,-5,-6,-7,8,9]
number_2=[x for x in num1 if x>0]
print(number_2)


n=int(input("Enter the limit="))
print([x*x for x in range(n+1)])

word=input("Enter a word=")
vowel=["A","E","I","O","U","a","e","i","o","u"]
listv=[x for x in word if x in vowel ]
print(listv)

word=input("Enter a word=")
listo=[ord(x) for x in word]
print(listo)

