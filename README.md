##  Languages or Frameworks Used
The program was created with Python.


# Code Explaination

int_to_roman function:

This function takes an integer num as input and returns its Roman numeral representation.
It starts by defining a dictionary called roman_numerals, which maps integer values to their corresponding Roman numeral symbols.
It initializes an empty string result to store the Roman numeral representation.
It iterates through the roman_numerals dictionary in descending order of integer values.
For each key-value pair in the dictionary, it checks if the input number num is greater than or equal to the integer value.
If num is greater than or equal to the integer value, it appends the corresponding Roman numeral symbol to the result string and subtracts the integer value from num.
It continues this process until num becomes zero.
Finally, it returns the result string containing the Roman numeral representation.


try-except block:

This block handles input from the user and ensures that the program doesn't crash due to invalid input.
It prompts the user to enter an integer using the input() function, converts the input string to an integer using int(), and assigns it to the variable user_input.
It then checks if the user_input is within the valid range (1 to 3999). If not, it prints a message asking the user to enter a valid integer.
If the input is valid, it calls the int_to_roman function with user_input as the argument and prints the Roman numeral representation.
If the user enters a non-integer value (e.g., a string), the ValueError exception is caught, and it prints a message asking the user to enter a valid integer.

## 🌟 How to run

`python Converting_Roman_to_Integer.py` to execute the code.


## 🤖 Author

[Piyush Sharma](https://github.com/Piyush8378)


