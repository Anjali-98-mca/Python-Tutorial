"""ccept a file name from user and print extension of that."""


file_name=input("Enter the filename with extension=")
li=file_name.split(".")
print("file extension=" +li[-1])
