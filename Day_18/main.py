import sys as s;
# x = input("Enter 1st number");
# a = int(x);
# y = input("Enter 2nd number");
# b = int(y);
# z = a+b;
# print (z);

x = int(input("Enter 1st number"));
y = int(input("Enter 2nd number"));
z = x+y;
print(z);

ch = input("Enter the char")[0];
print(ch);

data = eval(input("Enter expression"));
print(data);

a = int(s.argv[1]);
b = int(s.argv[2]);
c = a+b;
print(c);


In this lecture we are discussing about:
How to get user input
input function
printing input message
Type of input data
When to use index value
eval function
Passing values from command line
Argument line input

#1 How to get user input
# -- Getting user input in Python is straightforward. You can use the input() function 
# to get input from the user. The input function takes a single argument, which is the 
# prompt message displayed to the user.

#2 input function 
# -- In Python, the input() function is used to accept user input from the command line or console.
# name=input("Enter your name:");
# print(name);
# -- In this example, the input() function prompts the user to enter their name. Whatever the user types 
# in response is stored in the name variable.
# -- Note that the input() function always returns a string, so if we want to use the user's input as a number, 
# we'll need to convert it using the appropriate type-casting function (e.g., int() for integers or float() for 
# floating-point numbers).

#3 Types of input data
# -- The input() function always returns a string, regardless of what the user enters. 
# we may need to convert the input to a different data type if you want to perform calculations or other operations on it.

# e.g
# x=input("Enter first number: ");
# a=int(x);
# the input entered by the user is converted to an integer using the int() function in this example.

#4 when to use index value 
# -- If you want to get a single character from the user, we can use the input() function and index the result.

#5 eval function
# eval function
# -- The eval() function in Python is used to evaluate an expression entered by the user as a string. 
# The eval() function returns the result of the expression as a value.

# Passing values from command line
# -- sys module provides access to any command-line arguments via the sys.argv list. 
# we can pass arguments to a Python script from the command line using the sys.argv list. 
# The first argument in the list is always the name of the script itself.

# in command line we have to run this file
#python3 Mycode.py 9 5
            # 0      1 2

# Note: Mycode is count as 0th argument
#       9 is count as 1st argument
#       5 is count as 2nd argument