def check_eligibility(age):
    print("\nAge Eligibility Results:")
    print("-" * 30)
    
    # Voting eligibility
    if age >= 18:
        print("✓ Voting: Eligible")
    else:
        print("✗ Voting: Not eligible (minimum age: 18)")
    
    # Driving license eligibility
    if age >= 18:
        print("✓ Driving License: Eligible")
    else:
        print("✗ Driving License: Not eligible (minimum age: 18)")
    
    # Drinking alcohol eligibility
    if age >= 21:
        print("✓ Drinking Alcohol: Eligible")
    else:
        print("✗ Drinking Alcohol: Not eligible (minimum age: 21)")
    
    # Smoking eligibility
    if age >= 18:
        print("✓ Smoking: Eligible")
    else:
        print("✗ Smoking: Not eligible (minimum age: 18)")
    
    # Gambling eligibility
    if age >= 21:
        print("✓ Gambling: Eligible")
    else:
        print("✗ Gambling: Not eligible (minimum age: 21)")
    
    # Military service eligibility
    if age >= 18:
        print("✓ Military Service: Eligible")
    else:
        print("✗ Military Service: Not eligible (minimum age: 18)")
    
    # Senior citizen benefits eligibility
    if age >= 60:
        print("✓ Senior Citizen Benefits: Eligible")
    else:
        print("✗ Senior Citizen Benefits: Not eligible (minimum age: 60)")
    
    # Retirement eligibility
    if age >= 65:
        print("✓ Retirement: Eligible")
    else:
        print("✗ Retirement: Not eligible (minimum age: 65)")
    
    # R-rated movie eligibility
    if age >= 17:
        print("✓ R-Rated Movie: Eligible")
    else:
        print("✗ R-Rated Movie: Not eligible (minimum age: 17)")
    
    # Part-time job eligibility
    if age >= 14:
        print("✓ Part-time Job: Eligible")
    else:
        print("✗ Part-time Job: Not eligible (minimum age: 14)")

def main():
    print("Age Eligibility Checker")
    print("-" * 30)
    
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0:
                print("Age cannot be negative. Please try again.")
                continue
            check_eligibility(age)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
