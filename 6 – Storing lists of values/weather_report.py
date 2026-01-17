rainy_days = input("Which days had rain? ")
rainy_days_split = rainy_days.split()
array_length= len(rainy_days_split)

print("Number of days without rain: " + str( 7 - array_length))

