x = 1;

while(x<=3):
    print("Hello");
    x+=1;
# ---------------------------------
y = 4;
z = 1;

while(y>0):
    print("Bye");
    while(z<=2):
        print("Test");
        z+=1;

    y-=1;
# ---------------------------------
r = 1;
while(r<=5):
    print("Hello ", end="");
    s = 1;
    while(s<=3):
        print("World ", end="");
        s+=1;
    
    r+=1;
    print();


# Loops in Python language
# What is the use of loops?
# While loop and its implementation
# Syntax of the while loop
# Nested while loops in python
# What is the 'end' parameter in python?

# We can execute a statement multiple times, by using the loops.
# There are two types of a loop:
# 1. For loop
# 2. While loop

# In the while loop, we need a counter to count the number of times, a statement can be executed.
# We also have to put a condition in a while loop to repeat a statement until the given condition is satisfied.
# The while Loop. With the while loop, we can execute a set of statements as long as a condition is true.
# When the condition becomes false, the line immediately after the loop in the program is executed.
# The value of the counter will increase or decrease until the condition gets false.

# Syntax of the while loop:-
#  counter variable
#  while (condition):
#   statements;
#   incrementation/ decrementation

# So, there must be three things in a while loop:-
# 1. Initialization
# 2. Condition
# 3. Increment / Decrement
# Nested while loops can also be used in Python.
# Nested while loop simply means that a loop inside another loop.

# To print the values in the same, we use (end=" "). The value will not come in the new line after using it.
# Passing the whitespace to the end parameter (end=' ') indicates that the end character has to be identified by whitespace and not a new line.