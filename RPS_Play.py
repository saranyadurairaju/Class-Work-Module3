# Incorporate the random library
import random
# Print Title
print("Let's Play Rock Paper Scissors!")
# Specify the three options by defining a list
options = ["r", "p", "s"]
# Computer Selection
computer_choice = random.choice(options)
# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")
print(f"computer choice is: {computer_choice}")
# Run Conditionals
if user_choice == computer_choice:
    print(f"Both players selected {user_choice}.It is a tie")
elif user_choice == "r":
     if computer_choice == "s":
       print("Rock smashes the scissors! You win!")
     else:
        print("Paper covers rock! You lose.")
elif user_choice == "p":
    if computer_choice == "r":
        print("Paper covers the rock! You Win!")
    else:
         print("Scissors cuts the paper! You lose")
elif user_choice == "s":
    if computer_choice == "r":
        print("rock smashes scissors! you lose")
    else:
            print("scissors cuts the paper! You win!")