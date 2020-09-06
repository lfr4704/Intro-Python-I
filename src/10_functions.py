# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
num = None
def take_input():
    num = input("Enter a number: ")
    num = int(num)
    if not isinstance(num, int):
        print("This entry is invalid")
    return num

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

def check_if_even(num):
    if num % 2 == 0:
        print(f'{num} is a even number!')
    else:
        print(f'{num} is not an even number :(!')
    return num

take_input()
check_if_even(num)
