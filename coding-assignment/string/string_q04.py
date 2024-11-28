#Q4 =  You are given a name and a positive integer. You are required to print a greeting message using the name and a number.


# First we need to take the name as string from user input
name = input()

# Now, we need to take an integer representing the number of exclamation marks
num = int(input())

# TODO: Now you need to print the greeting message using the name and the number of exclamation marks. 
# You need to use the String formatting techniques here. There are several ways to 
# format strings in python, choose the one you are most comfortable with.
print(f'Hello, {name}{"!" * num}')