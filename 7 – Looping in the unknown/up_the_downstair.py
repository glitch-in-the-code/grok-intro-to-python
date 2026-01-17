
steps_str = input("How many steps? ")
steps = int(steps_str)
end_spaces = steps * 2

print("__")
for x in range(1, steps):
    spaces = x * 2

    for y in range(spaces):
        print(" ", end = "")

    print("|_")    

print(str("__"  * steps + "|"))