# Function to calculate BMI
def calc_bmi(weight_kg, height_m):    # renamed params for clarity
    """Calculate BMI using the standard formula"""
    result = weight_kg / (height_m ** 2)
    return result

# Function to determine what BMI category someone falls into
def get_bmi_category(bmi_value):
    # TODO: Maybe add more specific categories later?
    if bmi_value < 18.5:
        category = "Underweight "
    elif bmi_value >= 18.5 and bmi_value < 24.9:    # being explicit with the range
        category = "Normal weight "
    elif bmi_value >= 25 and bmi_value < 29.9:
        category = "Overweight "
    else:
        category = "Obesity "
    
    return category

# Get input from user
print("=== BMI Calculator ===")    # added a header for better UX
try:
    user_weight = float(input("Enter your weight (in kilograms): "))
    user_height = float(input("Enter your height (in meters): "))
    
    # Validate inputs are positive
    if user_weight <= 0 or user_height <= 0:
        print(" Weight and height must be positive values!")
    else:
        # Calculate the BMI
        calculated_bmi = calc_bmi(user_weight, user_height)
        bmi_cat = get_bmi_category(calculated_bmi)
        
        # Show the results to user
        print(f"\nYour BMI is: {calculated_bmi:.2f}")
        print(f"Category: {bmi_cat}")
        
        # Also display as markdown if in Jupyter
        try:
            md(f"### Your BMI is: **{calculated_bmi:.2f}**\n#### Category: {bmi_cat}")
        except:
            pass    # markdown display might not work in all environments

except ValueError:
    print("Please enter valid numeric values for weight and height.")
except Exception as e:    # catch any other unexpected errors
    print(f"An error occurred: {e}")
