names = input("Students: ")
names_array = names.split()
names_array.sort()

print("Class Roll")
for name in names_array:
	print(name)
