# Variables in Python
# Memory area of variables in Python
# How to get the address of a variable?
# Garbage collection
# Data types in Python

num = 10;
print(id(num));

name = "Test";
print(id(name));

a = 5;
b = a;
print(id(a));
print(id(b));
print(id(5));

z = 5;
print(id(z));

a = 6;
print(id(a));
print(id(b));

PI = 3.14;
print(PI);
PI = 3.16;
print(PI);
print(type(PI));

# Every variable has its address.
# In Python, the id() function is used to get the address of a variable.
# We can also assign the value of one variable to any other variable.
# In python, whenever you create multiple variables and if they have the same data then they will point towards the same box or same memory area.
# Everything is an object in Python.
# Variables are also known as tags as we tag the value with a variable.
# If the same variable store multiple values, then that variable will point towards the new memory area where the new value is get stored.

# If there is any data present in the memory that is not referenced by any variable, then that will be removed from the memory by the Garbage collector.

# The value of variables can be changed but the value of the constant remains the same.
# In python, we represent constants through capital letters.
# type() function is used to get the data type of value of a variable.
# Besides in-built data types, we can also create our own types.