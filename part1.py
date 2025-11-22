# script1_basics.py
"""
Demonstrating basic Python data types and user input
"""

print("=== Python Basic Types Demonstration ===")

# String type
name = input("Enter your name: ")
greeting = "Hello, " + name + "! Welcome to Python."

# Integer type
age = int(input("Enter your age: "))
birth_year = 2024 - age

# Float type
height = float(input("Enter your height in meters: "))

# Boolean type
is_student = input("Are you a student? (yes/no): ").lower() == "yes"

# List type
favorite_colors = []
print("Enter your 3 favorite colors:")
for i in range(3):
    color = input(f"Color {i+1}: ")
    favorite_colors.append(color)

# Tuple type
coordinates = (40.7128, -74.0060)  # New York coordinates

# Dictionary type
user_info = {
    "name": name,
    "age": age,
    "height": height,
    "is_student": is_student
}

# Set type
unique_letters = set(name.lower())

# Display all values
print("\n" + "="*50)
print("USER INFORMATION SUMMARY:")
print(f"Greeting: {greeting}")
print(f"Name: {user_info['name']}")
print(f"Age: {age} (Born in {birth_year})")
print(f"Height: {height} meters")
print(f"Student Status: {is_student}")
print(f"Favorite Colors: {favorite_colors}")
print(f"Sample Coordinates: {coordinates}")
print(f"Unique letters in your name: {unique_letters}")
print(f"User Info Dictionary: {user_info}")