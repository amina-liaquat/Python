# Temperature converter - simple utility I made for quick conversions
def celsius_to_fahrenheit(c):
    # Classic formula for C to F conversion
    fahrenheit = (c * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(f):
    # Converting F back to C
    celsius = (f - 32) * 5/9
    return celsius


print("🌡️ Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Choose an option (1 or 2): ")

# Let's check what the user picked
if choice == "1":
    celsius = float(input("Enter temperature in Celsius: "))
    result = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C = {result:.2f}°F")

elif choice == "2":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    result = fahrenheit_to_celsius(fahrenheit)
    # Printing the result with 2 decimal places for readability
    print(f"{fahrenheit}°F = {result:.2f}°C")

else:
    # Handle invalid input
    print("❌ Invalid choice. Please select 1 or 2.")
