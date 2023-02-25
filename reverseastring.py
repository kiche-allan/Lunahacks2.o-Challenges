def reverse_string(string):
    return string[::-1]

string = input('Enter a string: ')
reversed_string = reverse_string(string)
print(" The reversed string is: ", reversed_string)

# The def statement defines a new function called reverse_string that takes a single argument called s.
# The function returns s[::-1], which is a slice of s that starts at the end of the string (-1) and goes all the way to the beginning of the string (None).
# The step size for the slice is -1, which means that we are slicing the string in reverse order.
# Therefore, the result of s[::-1] is the reversed string.
# The input function prompts the user to enter a string and waits for the user to input a value. The input value is stored in the s variable.

# The reversed_s variable is assigned the value returned by the reverse_string function when called with the s argument.
# The print function outputs a message to the console, followed by the reversed_s value. The message is displayed in the console along with the reversed string and 