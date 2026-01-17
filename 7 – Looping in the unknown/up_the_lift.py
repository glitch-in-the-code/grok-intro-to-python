current_floor = int(input("Current floor: "))
destination_floor = int(input("Destination floor: "))

for i in range(current_floor, destination_floor + 1):
  print ("Level " + str(i))