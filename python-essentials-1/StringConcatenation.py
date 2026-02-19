def user_information():
    # Take name inputs
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    age_str = input("Enter your age: ")

    try:
        # Convert age to an integer
        age = int(age_str)

        # Check if the age is negative
        if age < 0:
            print("Age cannot be negative")
        else:
            # Create full name using string concatenation
            full_name = first_name + " " + last_name
            print("Full Name: " + full_name)
            
            # Calculate and print age next year
            age_next_year = age + 1
            print(f"You will be {age_next_year} next year")

    except ValueError:
        # Handles cases where the age cannot be converted to an integer
        print("Invalid age input")

if __name__ == "__main__":
    user_information()