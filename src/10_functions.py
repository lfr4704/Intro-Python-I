# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard

# def take_input():
#     try:
#         num = int(input("Enter a number: "))
#         print(num)
#     except ValueError:
#         print("This entry is invalid")

def take_input():
        num = input("Enter a number: ")
        if num.isdigit():
            return int(num)
        else:
            print("This entry is invalid")


# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

def check_if_even(num):
    if num % 2 == 0:
        print(f'{num} is a even number!')
    else:
        print(f'{num} is not an even number :(!')

#take_input()
check_if_even(take_input())
