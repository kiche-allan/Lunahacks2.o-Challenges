def roman_to_int(roman):
    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
    }
    
    result = 0
    prev_value = 0
    
    for char in roman[::-1]:
        value = values[char]
        if value < prev_value:
            result -= value
        else:
            result += value
            
        prev_value = value
        
        return result
print(roman_to_int('MCMXCIV'))
print(roman_to_int('IX'))
print(roman_to_int('IV'))


# The def statement defines a new function called roman_to_int that takes a single argument called roman.
# The values dictionary maps Roman numeral characters to their corresponding integer values.
# The result variable is initialized to zero. This variable will accumulate the integer value of the Roman numeral string as we iterate through it.
# The prev_value variable is also initialized to zero. This variable will keep track of the previous integer value that we encountered, so that we can determine whether to add or subtract the current value from the result.
# The for loop iterates over each character in the reversed roman string (reversed because we want to process the Roman numeral from right to left).
# For each character, we look up its corresponding integer value from the values dictionary.
# We then compare this value to the previous value we encountered. If the current value is less than the previous value, we subtract it from the result. Otherwise, we add it to the result.
# Finally, we update prev_value to be the current value, so that we can use it for the next iteration.
# Once the loop is done, we return the result variable, which now contains the integer value of the Roman numeral string.
    