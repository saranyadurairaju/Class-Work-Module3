# Number Chain

user_continue = "y"
initial_value = 0
while user_continue.lower() == "y":
    user_input = input("How many numbers?")
    for number in range(int(user_input)):
        print(initial_value + number + 1)
    user_continue = input("Do you want to continue(y/n): ")
    initial_value = initial_value + number + 1
