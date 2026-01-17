time_launch = int(input("Time to launch: "))
print("Counting down ...")
while time_launch > 0:
  print(str(time_launch) + " ...")
  time_launch = time_launch - 1

print("Lift Off!")