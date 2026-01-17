answer = "electricity"
print("What is my favourite food?")
guess = input("Guess? ")

stop_guessing = False

while stop_guessing == False:
  if  guess == answer:
     print("You guessed it! Buzzzz")
     stop_guessing = True 
  else:
     print("Not even close.")
     guess = input("Guess? ")
    
