
def equal():
    user_num1 = int(input("Give a number from 1-500: "))
    user_num2 = int(input("Give another number from 1-500: "))

    if user_num1 == user_num2:
            print("These numbers are equal")
    elif user_num1 < 1 or user_num1 > 500:
        print("Choose numbers within range")
    elif user_num2 < 1 or user_num2 > 500:
        print("Choose numbers within range")
    else:
        print("These numbers are not equal")

equal()

# Victor Moreno
# 3/7/24

# Function that takes two inputs from a user and prints whether they are equal or not.
