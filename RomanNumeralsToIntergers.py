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
    