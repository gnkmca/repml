import os
path = "abc.txt"
if os.path.isdir(path):
	print("It is a directory")
elif os.path.isfile(path):
	print("It is a file path")
else:
	print("It is not a file")
print()
