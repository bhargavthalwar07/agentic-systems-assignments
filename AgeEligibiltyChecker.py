def check_age_and_eligibility():
    # Take name and age inputs
    name = input("Enter your name: ")
    age_str = input("Enter your age: ")

    try:
        # Convert age to an integer
        age = int(age_str)

        # Check for negative age first
        if age < 0:
            print("Age cannot be negative")
        else:
            # Greet the user
            print(f"Hello {name}")
            
            # Determine and print the age category
            if age < 13:
                print("You are a Child")
            elif age <= 17:
                print("You are a Teenager")
            elif age <= 59:
                print("You are an Adult")
            else:
                print("You are a Senior Citizen")

            # Determine and print voting eligibility
            if age >= 18:
                print("You are eligible to vote")
            else:
                print("You are not eligible to vote")

    except ValueError:
        # Handles cases where the age cannot be converted to an integer
        print("Invalid age input")

if __name__ == "__main__":
    check_age_and_eligibility()