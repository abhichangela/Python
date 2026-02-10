a=6;
b=7;

# suppose we have two variables a and b and we want to swap the value of a and b
# we can do this by directly assigning the value of b to a and a to b lead to loose of value of a and b 
# we can do this by using temp variable
# we can do this by using xor operator
# we can do this by using python technique

# Method-1
# temp = a;
# a = b;
# b = temp;

# Method 2
# a = a + b;
# b = a - b;
# a = a - b;

# Method 3
# a = a ^ b;
# b = a ^ b;
# a = a ^ b;

# Method 4
# a,b = b,a;

print(a,b);

