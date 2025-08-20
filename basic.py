# # This is a simple Python script to demonstrate basic programming concepts
# # It calculates the sum of two numbers and prints the result
# a=3
# b=4
# sum = a + b
# print("The sum of", a, "and", b, "is", sum)

# # Now, let's take input from the user for a more interactive experience
# a=input("Enter first number: ")  # Input will be treated as a string
# b=input("Enter second number: ")
# sum = a + b
# print("The sum of", a, "and", b, "is", sum)

# # Note: The above input will concatenate strings, not add numbers.
# # To fix this, we need to convert the inputs to integers
# a = int(input("Enter first number: "))  # Convert input to integer
# b = int(input("Enter second number: "))
# sum = a + b
# print("The sum of", a, "and", b, "is", sum)

# # Demonstrating string concatenation
# name1 = 'Chirag Agrawal'              # Demonstrating different ways to define strings
# name2 = "Chirag Agrawal's assignment" # Double quotes is used for English strings
# name3 = '''Chirag 
# Agrawal'''                            # Triple quotes can be used for multi-line strings
# print(name1)
# print(name2)
# print(name3)

# # Demonstrating string formatting
# print(name1.upper())  # Converts string to uppercase
# print(name2.lower())  # Converts string to lowercase

# # Demonstrating arithmetic operations
# y = 7+8
# print(y)

# # Demonstrating line continuation
# y1 = 7+\
# 8
# print(y1)  # This will print 15, demonstrating line continuation with backslash

# # Demonstrating incorrect line continuation
# # y2 = 7 + 
# # 8
# # print(y2)  # This will raise a syntax error due to incorrect line continuation

# name='Chirag Agrawal\'s book'  # Using backslash to escape single quote in string
# print(name)

# # Demonstrating boolean expressions
# print(3 == 4)  # This will print False since 3 is not equal to 4
# print(3 != 4)  # This will print True since 3 is not equal to 4
# print(3 < 4)   # This will print True since 3 is less than 4
# print(3 > 4)   # This will print False since 3 is not greater than 4
# print(3 <= 4)  # This will print True since 3 is less than or equal to 4
# print(3 >= 4)  # This will print False since 3 is not greater than or equal to 4
# print(True+True)    # This will print 2 since True is treated as 1
# print(True+False)   # This will print 1 since True is treated as 1 and False as 0
# print(False+False)  # This will print 0 since both are False

# # Demonstrating string operations
# print("S"+"a") # This will print "Sa" since it concatenates the two strings
# print("S"*3)   # This will print "SSS" since it repeats the string 3 times

# # Demonstrating string indexing and slicing
# s = "Chirag Agrawal"
# print(s[0])         # This will print 'C', the first character of the string
# print(s[1])         # This will print 'h', the second character of the string
# print(s[6])         # This will print ' ', the seventh character of the string
# print(s[-1])        # This will print 'l', the last character of the string
# print(s[0:5])       # This will print 'Chira', the first five characters of the string
# print(s[7:])        # This will print 'Agrawal', from the eigth character to the end
# s[0] = "D"          # This will raise an error since strings are immutable in Python
# s.replace("C", "D") # This will replace 'C' with 'D' in the string, but does not modify the original string

# # Demonstrating complex numbers
# x=3+5j
# print(x)  # This will print the complex number (3+5j)

# # Demonstrating list operations
# list_1 = [1, 2, 3, 4, "Chirag", [1, 2, 3, 4]]  # A simple list of integers
# print(list_1)      # This will print the entire list
# print(list_1[0])   # This will print the first element of the list, which is 1
# print(list_1[4])   # This will print the fifth element of the list, which is "Chirag"
# print(list_1[5])   # This will print the sixth element of the list, which is another list [1, 2, 3, 4]
# print(list_1[-3])  # This will print the third last element of the list, which is 4

# # Demonstrating tuple operations
# tuple_1 = (1, 2, 3, 4, "Chirag", [1, 2, 3, 4])  # A simple tuple of integers
# print(tuple_1)      # This will print the entire tuple
# print(tuple_1[0])   # This will print the first element of the tuple, which is 1
# print(tuple_1[4])   # This will print the fifth element of the tuple, which is "Chirag"
# print(tuple_1[5])   # This will print the sixth element of the tuple, which is another list [1, 2, 3, 4]
# type(tuple_1)       # This will print <class 'tuple'> since tuple_1 is a tuple
# tuple_2=(7)         # This is not a tuple, it's just an integer
# type(tuple_2)       # This will print <class 'int'> since tuple_2 is not a tuple but an integer
# tuple_3=(7,)        # This is a tuple with one element

# # Demonstrating set operations
# set_1 = {1, 2, 3, 4, "Chirag", (1, 2, 3, 4),[1, 2, 3, 4]}  # A simple set of integers and a tuple and a list
# # Note: Sets do not allow mutable types like lists, so the list will be ignored
# print(set_1)       # This will print the entire set
# print(1 in set_1)  # This will print True since 1 is in the set
# print(5 in set_1)  # This will print False since 5 is not in the set
# print(set_1[0])    # This will raise an error since sets do not support indexing


# # Demonstrating the use of for loop

# for word in "Aaditya":
#     print(word,"hi")       # This will print each character in the string "Chirag" followed by "hi"

# for ele in [1, 2, 3, 4, 5]:    
#     print(ele)             # This will print each element in the list [1, 2, 3, 4, 5]
    
# for digit in 1234567890:
#     print(digit)           # This will raise an error since integers are not iterable, we need to convert it to a string first

# for ele in range(1,5):
#     print(ele)             # This will print numbers from 1 to 4 (5 is not included)
    
# # range(start,stop,step-size)

# d=range(1,10)  # This will create a range object from 1 to 9
# print(d)          # This will print the range object, which is not very informative
# print(list(d))    # This will convert the range object to a list and print it, which will show [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(tuple(d))   # This will convert the range object to a tuple and print it, which will show (1, 2, 3, 4, 5, 6, 7, 8, 9)
# print([*d])             # This will unpack the range object into a list, which will show [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print((*d,))            # This will unpack the range object into a tuple, which will show (1, 2, 3, 4, 5, 6, 7, 8, 9)