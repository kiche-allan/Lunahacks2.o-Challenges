def int_to_rom(num):
    values = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I'),


    ]
    
    result = ''
    
    for value, symbol in values:
        while num >= value:
            result += symbol
            num -= value
            return result
print(int_to_rom(3))


# The def statement defines a new function called int_to_roman that takes a single argument called num.
# The values list contains tuples that pair integer values with their corresponding Roman numeral symbols. The tuples are sorted in descending order by value, so that we can build up the Roman numeral string from left to right.
# The result variable is initialized to an empty string. This variable will accumulate the Roman numeral string as we iterate through the values list.
# The for loop iterates over each tuple in the values list.
# For each tuple, we check whether num is greater than or equal to the integer value. If it is, we add the corresponding Roman numeral symbol to the result string and subtract the integer value from num.
# We continue doing this until num is less than the current integer value. At this point, we move on to the next tuple in the values list.