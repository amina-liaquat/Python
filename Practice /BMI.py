# Importing required module
from IPython.display import Markdown as md

# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Function to interpret BMI category
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight "
    elif 18.5 <= bmi < 24.9:
        return "Normal weight "
    elif 25 <= bmi < 29.9:
        return "Overweight "
    else:
        return "Obesity "

# Input from user
try:
    weight = float(input("Enter your weight (in kilograms): "))
    height = float(input("Enter your height (in meters): "))

    # BMI calculation
    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)

    # Display result
    md(f"### Your BMI is: **{bmi:.2f}**\n#### Category: {category}")

except ValueError:
    print("❌ Please enter valid numeric values for weight and height.")
