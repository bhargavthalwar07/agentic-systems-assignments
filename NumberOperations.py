def calculate_numbers():
    try:
        # Take input from the user
        num1_str = input("Enter the first number: ")
        num2_str = input("Enter the second number: ")

        # Convert inputs to integers
        num1 = int(num1_str)
        num2 = int(num2_str)

        # Calculate and print the sum
        total_sum = num1 + num2
        print(f"Sum: {total_sum}")

        # Calculate and print the division result
        division = num1 / num2
        print(f"Division: {division}")

    except ValueError:
        # Handles cases where the input cannot be converted to an integer
        print("Invalid input")
        
    except ZeroDivisionError:
        # Handles cases where the second number is zero
        print("Cannot divide by zero")

if __name__ == "__main__":
    calculate_numbers()