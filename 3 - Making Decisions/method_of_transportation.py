raining = input("Is it currently raining? ")

if raining == "yes" or raining == "Yes":
  print("You should take the bus.")
else:
  distance = input("How far in km do you need to travel? ")  
  
  intdistance = int(distance)
  if intdistance > 10:
      print ("You should take the bus.")
      
  elif intdistance >= 2 and intdistance <= 10:
    print ("You should ride your bike.")
  elif intdistance > 0 and intdistance < 2:
    print("You should walk.")