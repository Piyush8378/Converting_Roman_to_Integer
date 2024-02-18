def int_to_roman(num):
   
    roman_numerals = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X',
        40: 'XL', 50: 'L', 90: 'XC', 100: 'C',
        400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
    }
    result = ''
    
    for value, numeral in sorted(roman_numerals.items(), reverse=True):
        
        while num >= value:     # Repeat the current numeral while num is greater than or equal to its value
            result += numeral
            num -= value
    return result

# take input

try:
    user_input = int(input("Enter an integer: "))
    if user_input <= 0 or user_input > 3999:
        print("Please enter an integer between 1 and 3999.")
    else:
        print("Roman numeral representation:", int_to_roman(user_input))
except ValueError:
    print("Please enter a valid integer.")
