def sum():
    user_input1 = int(input("Choose a number to add: "))
    user_input2 = int(input("Choose another number to add: "))

    user_sum = user_input1 + user_input2

    if user_sum == 10:
        print("Sum is equal to 10")
    elif user_sum < 10:
        print("Sum is less than 10")
    elif user_sum > 10:
        print("Sum is greater than 10")

sum()

# Victor Moreno
# 3/7/24

#Function takes two inputs from a user and prints whether the sum is greater than 10, less than 10, or equal to 10.
