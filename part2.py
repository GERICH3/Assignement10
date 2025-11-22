# script2_calculations.py
"""
Various mathematical calculations and operations
"""

print("=== Python Calculations and Operations ===")

# Basic arithmetic
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Mathematical operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "undefined (division by zero)"
modulo = num1 % num2 if num2 != 0 else "undefined"
exponentiation = num1 ** num2

# Area calculations
radius = float(input("Enter radius of a circle: "))
circle_area = 3.14159 * radius ** 2
circle_circumference = 2 * 3.14159 * radius

# Temperature conversion
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

# BMI calculation
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)

# Results
print("\n" + "="*50)
print("CALCULATION RESULTS:")
print(f"Basic Operations with {num1} and {num2}:")
print(f"  Addition: {num1} + {num2} = {addition}")
print(f"  Subtraction: {num1} - {num2} = {subtraction}")
print(f"  Multiplication: {num1} × {num2} = {multiplication}")
print(f"  Division: {num1} ÷ {num2} = {division}")
print(f"  Modulo: {num1} % {num2} = {modulo}")
print(f"  Exponentiation: {num1}^{num2} = {exponentiation}")

print(f"\nCircle with radius {radius}:")
print(f"  Area: {circle_area:.2f}")
print(f"  Circumference: {circle_circumference:.2f}")

print(f"\nTemperature Conversions:")
print(f"  {celsius}°C = {fahrenheit:.2f}°F")
print(f"  {celsius}°C = {kelvin:.2f}K")

print(f"\nBMI Calculation:")
print(f"  Weight: {weight} kg, Height: {height} m")
print(f"  BMI: {bmi:.2f}")