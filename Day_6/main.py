# Tuple
# Tuple is almost similar to a list in which we can store multiple values.
# Tuples are Immutable and we cannot change values in them.
# To define a tuple, () round brackets are used.
# We can fetch the values from a tuple using the index value that can be given in a square bracket.
# Tuple will give an error when you tried to change a value in it.

abc = (23,11,45,37, 11);
print(abc);
print(abc[2]);
print(abc.count(11));
abc[2] = 51; #we cannot change this value
print(abc);

# count method is used to count the occurrences of an element in a tuple. It counts the number of times that an element is present in a tuple.
# e.g., If an element of value 5 is present two times in a tuple, then the count method returns 2.

# We can use tuples when we want a list of multiple values but we do not want to change it.
# Iteration in the tuple is faster than the list.