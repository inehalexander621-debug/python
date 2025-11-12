# Task 1: Variable Practice
# Create a program that:
# 1. Declares variables of different data types
# 2. Performs operations between them
# 3. Demonstrates type conversion

# 1. Declare variables of different data types
integer_num = 10              # int
float_num = 5.5               # float
string_num = "20"             # string
boolean_val = True            # bool

# Display initial values and their types
print("Initial Values and Types:")
print(f"integer_num = {integer_num} ({type(integer_num)})")
print(f"float_num = {float_num} ({type(float_num)})")
print(f"string_num = {string_num} ({type(string_num)})")
print(f"boolean_val = {boolean_val} ({type(boolean_val)})")
print()

# 2. Perform operations between them
sum_result = integer_num + float_num     # int + float → float
bool_sum = integer_num + boolean_val     # int + bool → int (True = 1)
concat_result = str(integer_num) + string_num  # convert int → str for concatenation

print("Results of Operations:")
print(f"Sum of integer_num and float_num = {sum_result}")
print(f"Sum of integer_num and boolean_val = {bool_sum}")
print(f"Concatenation of integer_num and string_num = {concat_result}")
print()

# 3. Demonstrate type conversion
converted_int = int(string_num)           # string → int
converted_float = float(string_num)       # string → float
converted_str = str(float_num)            # float → string
converted_bool = bool(integer_num)        # int → bool

print("Type Conversion Examples:")
print(f"string_num ('{string_num}') to int: {converted_int} ({type(converted_int)})")
print(f"string_num ('{string_num}') to float: {converted_float} ({type(converted_float)})")
print(f"float_num ({float_num}) to string: '{converted_str}' ({type(converted_str)})")
print(f"integer_num ({integer_num}) to bool: {converted_bool} ({type(converted_bool)})")



# Task 2: Operator Challenge
# Write a program that:
# 1. Takes two numbers as input
# 2. Performs all arithmetic operations on them
# 3. Compares them using all comparison operators
# 4. Displays the results in a formatted way

# 1. Take two numbers as input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\n=== Arithmetic Operations ===")
# 2. Perform all arithmetic operations
print(f"Addition: {num1} + {num2} = {num1 + num2}")
print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
print(f"Multiplication: {num1} * {num2} = {num1 * num2}")

# Handle division carefully to avoid ZeroDivisionError
if num2 != 0:
    print(f"Division: {num1} / {num2} = {num1 / num2}")
    print(f"Floor Division: {num1} // {num2} = {num1 // num2}")
    print(f"Modulus: {num1} % {num2} = {num1 % num2}")
else:
    print("Division, Floor Division, and Modulus: Not possible (division by zero)")

print(f"Exponentiation: {num1} ** {num2} = {num1 ** num2}")

print("\n=== Comparison Operations ===")
# 3. Compare them using comparison operators
print(f"{num1} == {num2} ➜ {num1 == num2}")
print(f"{num1} != {num2} ➜ {num1 != num2}")
print(f"{num1} > {num2} ➜ {num1 > num2}")
print(f"{num1} < {num2} ➜ {num1 < num2}")
print(f"{num1} >= {num2} ➜ {num1 >= num2}")
print(f"{num1} <= {num2} ➜ {num1 <= num2}")

print("\n=== Program Complete ===")




# Task 3: Input Validation
# Create a user registration system that:
# 1. Takes username, email, and password as input
# 2. Validates each input (non-empty, proper format)
# 3. Confirms password match
# 4. Displays success message or error messages

import re  # for email validation using regular expressions

print("=== User Registration System ===")

# 1. Take inputs from the user
username = input("Enter username: ").strip()
email = input("Enter email: ").strip()
password = input("Enter password: ").strip()
confirm_password = input("Confirm password: ").strip()

# 2. Validation
errors = []

# Check for empty fields
if not username:
    errors.append("❌ Username cannot be empty.")
if not email:
    errors.append("❌ Email cannot be empty.")
if not password:
    errors.append("❌ Password cannot be empty.")
if not confirm_password:
    errors.append("❌ Please confirm your password.")

# 3. Check email format
email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
if email and not re.match(email_pattern, email):
    errors.append("❌ Invalid email format.")

# 4. Check if passwords match
if password and confirm_password and password != confirm_password:
    errors.append("❌ Passwords do not match.")

# 5. Display results
print("\n=== Registration Result ===")
if errors:
    for error in errors:
        print(error)
    print("\n⚠ Registration failed. Please fix the above issues.")
else:
    print(f"✅ Registration successful! Welcome, {username}!")



# # Task 4: Complete Application
# Build a temperature converter that:
# 1. Takes temperature value and unit (C/F) as input
# 2. Converts between Celsius and Fahrenheit
# 3. Handles invalid inputs gracefully
# 4. Displays the converted temperature  


print("=== Temperature Converter ===")

# 1. Take temperature value and unit as input
temp_input = input("Enter temperature (e.g., 36.5 C or 97.7 F): ").strip()

# 2. Try to parse input safely
try:
    # Split the input into value and unit
    value_str, unit = temp_input[:-1].strip(), temp_input[-1].upper()

    # Convert the numeric part to float
    value = float(value_str)

    # 3. Perform conversion based on the unit
    if unit == "C":
        converted = (value * 9/5) + 32
        print(f"{value:.2f}°C = {converted:.2f}°F")
    elif unit == "F":
        converted = (value - 32) * 5/9
        print(f"{value:.2f}°F = {converted:.2f}°C")
    else:
        print("❌ Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")

except ValueError:
    print("❌ Invalid input format. Please enter a number followed by C or F (e.g., 25 C or 77 F).")

print("\n=== Conversion Complete ===")