print(bin(20));
print(oct(32));
print(0b01010);
print(0o31);
print(0x34);

# In programming, the number system is a way of representing numbers using different bases.
# The most commonly used number systems in programming are the decimal (base 10), 
# binary (base 2), octal (base 8), and hexadecimal (base 16) systems.

# a)Decimal system: This is the number system we use in our everyday lives. It uses 10 digits (0-9) 
# to represent numbers.

# b)Binary system: This system uses only two digits (0 and 1) to represent numbers. It is commonly 
# used in computer systems because digital devices work with binary signals.

# c)Octal system: This system uses 8 digits (0-7) to represent numbers. It's often used in computer programming 
# because it's a compact way to represent binary numbers.

# d)Hexadecimal system: This system uses 16 digits (0-9 and A-F) to represent numbers. It's commonly used in computer programming 
# and web development to represent colors and memory addresses.

# Converting  different number systems:

# Decimal to binary: Divide the decimal number by 2 and write down the remainder. Keep dividing by 2 and writing down the remainders until 
# you get to 0 at quotient. Then, read the remainders in reverse order to get the binary number.
# e.g 51
#     2|51 |1
#     2|25 |1
#     2|12 |0
#     2|6  |0
#     2|3  |1
#     2|1  |1
#      |0  |1
# reverse order: 110011
# Binary to decimal: Multiply each digit in the binary number by the corresponding power of 2 
# (starting with 2^0 on the right). Add up the results to get the decimal number.

# e.g 11011
#     2^4 2^3 2^2 2^1 2^0
#     1*16 1*8 0*4 1*2 1*1
#     16+8+0+2+1=27
# It is Same for octal and hexadecimal(Not in this lecture but for your knowledge)

# Decimal to octal: Divide the decimal number by 8 and write down the remainder. Keep dividing by 8 and 
# writing down the remainders until you get to 0. Then, read the remainders in reverse order to get the 
# octal number.
# e.g 
#     51
#     8|51 |3
#     8|6  |6
#     8|0  |0
#     reverse order: 360
# Octal to decimal: Multiply each digit in the octal number by the corresponding power of 8 (starting with 8^0 on the right). 
# Add up the results to get the decimal number.
# e.g 
#     360
#     8^2 8^1 8^0
#     3*64 6*8 0*1
#     192+48+0=240

# Decimal to hexadecimal: Divide the decimal number by 16 and write down the remainder. If the remainder is 
# greater than 9, replace it with the corresponding letter (A-F). Keep dividing by 16 and writing down the remainders 
# until you get to 0. Then, read the remainders in reverse order to get the hexadecimal number.
# e.g 
#     51
#     16|51 |3
#     16|3  |3
#     16|0  |0
#     reverse order: 33

# Hexadecimal to decimal: Multiply each digit in the hexadecimal number by the corresponding power of 16 (starting with 16^0 on the right). 
# If a digit is a letter, replace it with the corresponding value (A=10, B=11, etc.). Add up the results to get the decimal number.
# e.g 
#     33
#     16^1 16^0
#     3*16 3*1
#     48+3=51

# Only for Interest (Not in this lecture)
# Converting from octal to binary and binary to octal can be done using a simple method.
# Conversion from Octal to Binary:

# To convert an octal number to binary, we can simply replace each digit in the octal number with its equivalent three-digit binary number. 
# Here are the octal-to-binary conversions for each octal digit:
# 0 = 000
# 1 = 001
# 2 = 010
# 3 = 011
# 4 = 100
# 5 = 101
# 6 = 110
# 7 = 111
# For example, to convert the octal number 725 to binary:
# 7 = 111
# 2 = 010
# 5 = 101
# So, 725 in octal is equivalent to 111010101 in binary.
# Conversion from Binary to Octal:
# To convert a binary number to octal, you can group the binary digits into sets of three (starting from the right) 
# and replace each set with its equivalent octal digit. Here are the binary-to-octal conversions for each set of three binary digits:
# 000 = 0
# 001 = 1
# 010 = 2
# 011 = 3
# 100 = 4
# 101 = 5
# 110 = 6
# 111 = 7
# For example, to convert the binary number 101011011 to octal:
# 1 0 1   0 1 1    0 1 1
# |- - - ||- - - | |- - - |
#  5       3        3
# we get 533 in octal.

# Use of method in python to direclty convert number system:
# Decimal to binary: bin()
# e.g 
#     bin(51)
#     '0b110011' # 0b represent binary formate
# binary to decimal: int()
# e.g 
#     int('0b110011',2)
#     51

# Decimal to octal: oct()
# e.g 
#     oct(51)
#     '0o63'  # 0o represent octal formate
# octal to decimal: int()
# e.g 
#     int('0o63',8)
#     51

# Decimal to hexadecimal: hex()
# e.g 
#     hex(51)
#     '0x33'  # 0x represent hexadecimal formate
# hexadecimal to decimal: int()
# e.g 
#     int('0x33',16)
#     51