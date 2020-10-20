# CSC 217 - Assignment Four - Lake County Recursion
# Programmer: Connor McCloskey
# Date created: 7/14/2020
# Date of final update: 7/17/2020


# Write-up -------------------------------------------------------------------------------------------------------------
"""
Wow, this was a tough one!

Recursion has, by far, been the most difficult concept for me to grasp. I guess that's why it's Advanced Python, right?
Still, I wish we were spending more time on it. I know it's a concept I'll have to continue practicing on.

A breakdown of the sections:
1) Variables and Imports - Wow! Look! Another bool Connor's using for his menus!
2) Functions - Contains all functions for this program. The only addition is a function to get array input from the user.

Per the grading rubric, I need to cite some code that I researched as part of this. My code for the 3rd function
(the permutations problem) comes mainly from this source: https://www.geeksforgeeks.org/generate-all-the-permutation-of-a-list-in-python/.
I had to do a fair amount of research to finally understand this algorithm, but failed to create my own original
implementation of it. A full explanation of the cited code is available below in the comments above the function as
requested in the rubric.

I hope this is okay, I was a bit confused by the fact the grading rubric says that researched code must be cited, but
the assignment itself says that all our examples must be our own. I am more than happy to have points deducted as if
I had incompleted this section, but I wanted to ensure that I understood what I was doing, understood the core concept
of the assingment, and turned in a more complete assignment.

3) Main program - Contains ye olde main menu. This one looks a bit more complicated due to the need to accommodate the
inputs required by some of the functions, but is really just the same code I've used before.
"""
# --------------------------------------------------------------------------------------------------------------------//

# Variables & Imports --------------------------------------------------------------------------------------------------
# Boolean for controlling menu loops
done = False
# --------------------------------------------------------------------------------------------------------------------//


# Functions ------------------------------------------------------------------------------------------------------------
# Function 1 - Count substrings w/ same first and last character
# Convert string to list for easier manipulation
# Count and cursor_index must start at 0
# If the string is empty, we obviously don't need to do anything, so return
# Essentially, the "cursor index" is element we're looking at to see if there are substrings made from it
# From the cursor, we loop through the array, searching for other elements with the same value
# Anytime there is, we increment the count of substrings by 1
# Once that is done, we call the function, incrementing the cursor index by one so we're looking at a new element to
# compare.
def count_substring(string, count, cursor_index):
    string = list(string)
    if len(string) == 0:
        return count
    else:
        if cursor_index > (len(string) -1):
            return count
        for i in range(cursor_index, len(string)):
            if string[i] == string[cursor_index] and i != cursor_index:
                count += 1
        cursor_index += 1
        count = count_substring(string, count, cursor_index)
    return count


# Function 2 - find length of string
# First, convert string to array for manipulation
# If the string is empty, return 0 for the length
# Else, remove an element of the string, add 1 to whatever is returned by teh recursive function call, and pass in the
# shorter string.
def string_length(string):
    string = list(string)
    if not string:
        return 0
    else:
        string.pop()
        return 1 + string_length(string)


# Function 3 - print all possible combinations of r elements in a given list of size n
"""
Okay! The researched one! I changed variable names as I continued to play with this to learn how it was working.
In a nutshell, the algorithm for this problem works as such:
1) Looping through the array, remove the selected element
2) Create a new, smaller array without that element
3) Recursively call the function
In doing so, we create the permutations by appending the first element to all possible permutations of the other elements.
That includes when we loop through this smaller array.
So, if are input was ABC, we would remove 'A', create 'BC' and 'CB' through the same process, and append 'A', then
move to the next item in the array via the loop.
Once we're done with the recursion, we print all elements in our new array containing all our permutations!
"""
def permutations(array):
    result = []
    if len(array) == 1:
        return [array]
    else:
        for i in range(len(array)):
            cursor_var = array[i]
            new_array = array[:i] + array[i + 1:]
            for j in permutations(new_array):
                result.append([cursor_var] + j)
    return result


# Function 4 - Find minimum of array
# The mirror to the maximum function
# Essentially, we compare an element in the array to our current min
# If the element in the array is smaller, swap it
# We continue to iterate through the array until we've done this at least once without making a swap
# Once that happens, we print the current min!
def minimum(array, i, current_min):
    if array[i] < current_min:
        current_min = array[i]
        i = 0
        minimum(array, i, current_min)
    elif i == (len(array) - 1):
        print("Min of array:", current_min)
        return
    else:
        i += 1
        minimum(array, i, current_min)


# Function 5 - Find maximum of array
# The mirror of the above minimum array, works the same way.
def maximum(array, i, current_max):
    if array[i] > current_max:
        current_max = array[i]
        i = 0
        maximum(array, i, current_max)
    elif i == (len(array) - 1):
        print("Max of array:", current_max)
        return
    else:
        i += 1
        maximum(array, i, current_max)


# Function 6 - Print a pattern
# Prints an upside-down right-triangle!
# This will be based on the number of lines the user wants to input
# If the number of lines we want to print is 0, we return
# Else, print the line, decrement the lines to print, then recursively call the function
def print_pattern(lines):
    if lines == 0:
        return
    else:
        print("*" * lines)
        lines -= 1
        if lines == 0:
            return
        else:
            print_pattern(lines)


# Function 7 - Product of two numbers
# Accepts two ints as input
# If either of the ints is zero...return zero!
# Else, add x to itself, using y as our control
# Thanks to the multiplictive property, doesn't matter which we use for addition
# Then, recursively call until done, then return the product
def mult(x, y, x_original):
    print("X:", x)
    print("Y:", y)
    if x == 0 or y == 0:
        return 0
    if y == 1:
        return x
    else:
        x += x_original
        y -= 1
        if y == 0:
            return
        else:
            return mult(x, y, x_original)


# A simple function to fill an array with user input
def getInputArray():
    menu_bool = False
    array = []
    print("""
You will now be prompted to enter in a series of integers for your array.
When you are done, enter in the command DONE (all caps) to proceed.    
    """)
    while not menu_bool:
        user_input = input("Enter array element: ")
        if user_input == "DONE":
            menu_bool = True
        else:
            try:
                modified_input = int(user_input)
            except ValueError:
                print("Invalid input. Please be sure to enter integers only.")
            else:
                array.append(modified_input)
    return array
# --------------------------------------------------------------------------------------------------------------------//


# Main Program ---------------------------------------------------------------------------------------------------------
print("Welcome to the 2020 McCloskey Lake County Recursion Simulator!  ")
while not done:
    print("""
Please select a menu item by entering the corresponding letter.

MAIN MENU
A) Count substrings in a string
B) Find the length of a string
C) Find all possible permutations of a list
D) Find minimum item of an array
E) Find maximum item of an array
F) Print a pattern based on input
G) Multiplication
H) Quit program
""")
    user_input = input("Your Selection: ")
    print("")
    if user_input.lower() == "a":
        user_input = input("Enter the string you'd like to find substrings in: ")
        result = count_substring(user_input, 0, 0)
        print("Substring total:", result)
    elif user_input.lower() == "b":
        user_input = input("Enter the string you'd like to find the length of: ")
        result = string_length(user_input)
        print("String length:", result)
    elif user_input.lower() == "c":
        array = getInputArray()
        permutations(array)
        print("Printing results...")
        for i in permutations(array):
            print(i)
    elif user_input.lower() == "d":
        array = getInputArray()
        minimum(array, 0, array[0])
    elif user_input.lower() == "e":
        array = getInputArray()
        maximum(array, 0, array[0])
    elif user_input.lower() == "f":
        print("This function will print an upside down triangle based on the number of lines you'd line to print.")
        user_input = input("Please enter the number of lines you'd like to print: ")
        try:
            modified_input = int(user_input)
        except ValueError:
            print("Invalid input. When using this function, please use only integers.")
        else:
            print_pattern(modified_input)
    elif user_input.lower() == "g":
        print("Now enter the numbers you would like to multiply.")
        x = input("First number: ")
        try:
            modified_x = int(x)
        except ValueError:
            print("Invalid input. When using this function, please use only integers.")
        else:
            y = input("Second number: ")
            try:
                modified_y = int(y)
            except ValueError:
                print("Invalid input. When using this function, please use only integers.")
            else:
                product = mult(modified_x, modified_y, modified_x)
                print("Product:", product)
    elif user_input.lower() == "h":
        quit(0)
    else:
        print("Invalid input. Please be sure to select a letter corresponding with an menu item.")
# --------------------------------------------------------------------------------------------------------------------//
