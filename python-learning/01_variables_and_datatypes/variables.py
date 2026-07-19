
message = "Hello World"
print(message)


# how to count the length of the string
print(len(message)) 


# how to access a specific character in the string
print(message[10]) 


# how to access a specific character in the string using negative indexing
print(message[-11])


# how to access a range of characters in the string
print(message[0:5]) # it print Hello
print(message[6:12]) # it print World
# here the first index is inclusive and the second index is exclusive


print('##############################################################################################################')

# data types in python

# Airthmetic Operators
# Addition:  3 + 2
# Subtraction:  3 - 2
# Multiplication:  3 * 2
# Division:  3 / 2
# Floor Division:  3 // 2
# Exponent: 3 ** 2
# Modulus: 3 % 2

# abs - Absolute Value
print(abs(-7.25)) # it print 7.25

# round - Round a number to a specified number of decimal places
print(round(7.25)) # it print 7
print(round(7.75, 1)) # it print 7.8


print('##############################################################################################################')

# comparison operators (returns boolean value True or False)
# Equal: 3 == 2
# Not Equal: 3 != 2
# Greater than: 3 > 2
# Less than: 3 < 2
# Greater than or equal to: 3 >= 2
# Less than or equal to: 3 <= 2

print(3 == 2) # it print False
print(3 != 2) # it print True
print(3 > 2) # it print True
print(3 < 2) # it print False
print(3 >= 2) # it print True
print(3 <= 2) # it print False

# Type casting in python
# int() - converts a value to an integer

num_1 = '100'
num_2 = '200'

print(num_1 + num_2) # it print 100200

# convert string to integer
num_1 = int(num_1)
num_2 = int(num_2)

print(num_1 + num_2) # it print 300