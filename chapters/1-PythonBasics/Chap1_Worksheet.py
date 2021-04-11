# Byte Size : Chapter 1 Python Worksheet

# The hashtag symbol at the start of the line marks this line as a COMMENT
# Comments in Python are intended for humans reading the file
# Python completely ignores any line that starts with a the hashtag symbol


# ---- THE PRINT COMMAND -------

# Let's start with the print command
# Print asks Python to display something on the screen
# Whatever is inside the parentheses after the print is what will be displayed

# The print statement below prints a greeting
# Change the text inside the parentheses to include your name
# Then run this Python file and it should print your modified greeting

# You need to keep the " marks so that Python knows
#     ... that the thing in parentheses is human text
#     ... and not a variable name or python command

print("Hello, Nameless Person")



# ---- MAKING VARIABLES ----

# We can save a value in a variable by using the = sign

# The = sign is an instruction in Python that asks Python
#     ... To take the value on the right
#     ... And store it in the variable name on the left

# If you remove the # sign from the line below, you can make an age variable
# Change the line of code that it uses your real age instead of 97

# age = 97

# Let's make sure this worked
#     ... you can uncomment the line below to print the value of age

# print(age)

# Often it is useful to print two things at the same time
# You can put two things inside the parentheses of a print statement
#     ... all you need to do is separate them with a comma
#     ... for example print( 1,  2) 

# Change the print statement to print both:
#     the words  "My age is "
#     as well as the value of age

# When you use an = sign, left and right matter a lot
# Try changing the age = 97 line so that it instead says 97 = age
# This should give you an error

# One final thing, when you are printing a lot of things in a Python progra
#    ... Sometimes you might want a blank line to space things out
# The line below just prints a blank line

# print( " " )

# ---- CHANGING VARIABLES ----

# Often we will want to change the value in a variable

# I assume that you still have the line up above giving a value to age
#   ... This is your age this year

# print( "This year my age is ",  age)

# Python can do basic math, so it is easy to figure out your age next year
# Just remove the # from the line below

# age = age + 1

# When Python sees this instruction,
#    ... Python first figures out what age + 1 (using the current value of age)
#    ... Then Python takes this new number (age + 1)
#             and stores that as the new value of age

# Below this point, any time you refer to age,
#      you will be referring to the new value of age
# Try it out, by writing a print statement that prints the new age,
#      which is your age next year


# Note that Python can do addition         3 + 2
#                         substraction     5 - 3
#                         multiplication   5 * 2
#                     and division         10 / 2


# --- INPUT FROM THE KEYBOARD ---

# Another way to get values to put in variables is to ask the user to type something
# The input statement asks the user to type something

# Remove the # sign from the statement below

# color = input("Enter Your Favorite Color: ")

# The input command does two things:
#     First it prints whatever message you put in the parentheses
#     Next it waits for the user to type something on the keyboard and press Enter
# Then the = sign in the line above puts whatever text they enter into the variable color

# Test this out by printing out a message about the favorite color



# -- PUT IT ALL TOGETHER ---

# Let's put togehter what we have been doing so far

# Write some Python instructions that ask someone for name
#     and their favorite animal
# Then print out some messages that includes their name and this animal


# NOTE: In a future worksheet we will discuss how to have Python do different things
#           depending on what the user types in as their favorite animal
#      For example, if they type "elephant" we could cheer for them
#           because elephants are awesome!!
