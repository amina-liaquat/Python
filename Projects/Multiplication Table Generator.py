# Multiplication Table Generator

# Ask user for the number
num = int(input("Enter a number to generate its multiplication table: "))

# Ask user for the range
end_range = int(input("Enter the range (e.g., 10 for 1 to 10): "))

print(f"\nMultiplication Table of {num}\n" + "-"*30)

# Loop to generate the table
for i in range(1, end_range + 1):
    print(f"{num} x {i} = {num * i}")

except ValueError:
    print("Please enter valid integers only.")
