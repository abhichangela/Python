num = 5;
print(type(num));
num = 4+8j;
print(type(num));
a = 5.6;
b = int(a);
print(b, type(b));
c = float(b);
print(c, type(c));
k = complex(a,b);
print(k, type(k));
print(a<b, a>b);
print(int(True), '---', int(False));

lst = [25,14,65,1];
print(type(lst));
tup = (10,98,74,30);
print(type(tup));
set = {12,43,3,54};
print(type(set), set);

print(range(10));
print(list(range(10)));
print(list(range(3,20,2)));

dir = {'abc': 'iPhone', 'pqr': 'Vivo', 'xyz': 'onePlus'};
print(dir, type(dir), dir.get('pqr'));
print(dir.keys());
print(dir.values());
t = None;
print(type(t));


# Python has several built-in data types. Here are some of the most common ones:

# i) NoneType: This is a special data type that represents the absence of a value. It is similar to null in other languages.
# ii) Numbers: These can be integers, floating-point numbers, or complex numbers.
# iii) Booleans: These are values that represent True or False.
# iv) Lists: These are ordered collections of objects, enclosed in square brackets.
# v) Tuples: These are similar to lists, but are immutable (i.e., their contents cannot be changed), and are enclosed in parentheses.
# vi) Sets: These are unordered collections of unique elements, enclosed in curly braces.
# vii) Strings: These are sequences of characters, enclosed in single or double quotes.
# viii) Ranges: These are immutable sequences of numbers, and are commonly used to iterate over a sequence of numbers in a for loop.
# ix) Dictionaries: These are collections of key-value pairs, enclosed in curly braces.

# i)None Type
# a=None
# type(a)

# ii)Numbers
# int: if you want to assign a integer value to a variable 
# a=5
# type(a)

# float: if you want to assign a float value to a variable 
# num =2.5 
# type(num) 

# complex: if you want to assign a complex value to a variable
# num =2+9j 
# type(num)

# type conversion:  if you want to convert one data type to another data type 
# a=5.6
# b=int(a) 
# type(b) # output : int
# k=float(b) 
# type(k) # output : float
# c=complex(4,5)
# type(c) # output : complex

# iii)boolean: if you want to assign a variable with a boolean value
# a= True
# type(a)  # output : bool
# bool=3 less then5 
# True 
# type(bool)
 
# Sequence data types : if you want to assign a variable with multiple values 
# List, Tuple, Set, String, Range.

# iv) List  if you want to assign a variable with multiple values and you want to change the values 
# -- In Python, a list is a collection of ordered and mutable elements enclosed
# in square brackets. Lists are one of the most commonly used data structures in 
# Python because of their versatility and flexibility.

# lst=[25,36,45,12]
# type(lst) # output : list

# v) Tuple:  if you want to assign a variable with multiple values and you donot want to change the values make immutable 
# -- In Python, a tuple is a collection of ordered and immutable elements enclosed in parentheses. 
# Tuples are similar to lists, but they cannot be modified once they are created, which makes them 
# useful for storing data that should not be changed during the program's execution.

# t=(25,36,45,12,7)
# type(t) # output : tuple

# vi) Set:  if you want to assign a variable with multiple values and you donot want to change the values and you donot want to duplicate values 
# -- In Python, a set is an unordered collection of unique elements enclosed in curly braces.
# Sets are useful for storing data that should not contain duplicates, such as a list of
# users on a website.

# s={25,36,45,12,25,36}
# type(s) # output : set
# #output: {36, 12, 45, 25}

# vii) String: if you want to assign sequence of characters to a variable
# -- In Python, a string is a sequence of characters enclosed in single or double quotes.
# Strings are immutable, which means that they cannot be modified once they are created.

# str = "hello"
# type(str) # output : str

# we are not talk about char data type in python
# st='a' # every character is a string in python

# viii) Range: if you want to assign a variable with multiple values and you don't want to change the values and you want to generate a sequence of numbers
# -- In Python, a range is a sequence of numbers that is immutable and iterable.
# Ranges are commonly used to iterate over a sequence of numbers in a for loop.

# range(10) # range data type
# type(range(10))  # output : range 
# list(range(2,10,2)) # output : [2, 4, 6, 8]

# ix) Dictionary:  if you want to assign a variable with multiple values and you donot want to change the values and you want to assign a key to each value 
# -- In Python, a dictionary is a collection of key-value pairs enclosed in curly braces.

# d={1:'a',2:'b',3:'c'}
# type(d)