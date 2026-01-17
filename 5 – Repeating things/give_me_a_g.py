import time

cheer = input("Cheer\]: ")

final_cheer = "Give me a {0}, {1}!"
for letter in cheer:
  new_str = final_cheer.format(letter, letter)
  print(new_str)
  time.sleep(0.1)
print("What does it spell?") 
uppercheer = cheer.upper()
print(uppercheer)