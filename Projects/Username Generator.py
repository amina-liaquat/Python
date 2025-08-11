import random

def generate_username():
    # Get user input and clean up
    first_name = input("Enter your first name: ").strip().lower()
    last_name = input("Enter your last name: ").strip().lower()
    
    # Handle empty inputs
    if not first_name or not last_name:
        print("Error: Both names are required!")
        return None
    
    # Create base username components
    first_initial = first_name[0]
    last_part = last_name.replace(' ', '')[:8]  # Remove spaces and limit to 8 chars
    
    # Generate random number
    random_num = random.randint(0, 999)
    formatted_num = f"{random_num:03d}"  # 3-digit number with leading zeros
    
    # Combine components
    username = f"{first_initial}{last_part}{formatted_num}"
    
    return username

# Generate and display username
if __name__ == "__main__":
    username = generate_username()
    if username:
        print(f"Generated username: {username}")
