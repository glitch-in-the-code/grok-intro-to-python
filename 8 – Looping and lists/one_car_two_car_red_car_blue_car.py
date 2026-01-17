cars_case = input("Cars: ")
cars = cars_case.lower().split()  
total_red_int = 0
total_blue_int = 0

for car in cars:
    if car == "red":
        total_red_int = total_red_int + 1  
    if car == "blue":
        total_blue_int = total_blue_int + 1

total_red = str(total_red_int)
total_blue = str(total_blue_int)
        
  
print("red: " + total_red)
print("blue: " + total_blue)
