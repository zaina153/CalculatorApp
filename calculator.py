
from add import add
from subtract import subtract
from multiply import multiply
from divide import divide

# Print menu
print("Select operation:")
print("A. Add")
print("S. Subtract")
print("M. Multiply")
print("D. Divide")

# Main loop
while True:
    choice = input("Enter choice (A/S/M/D): ").upper()  # Convert input to uppercase

    if choice in ('A', 'S', 'M', 'D'):
        num1 = float(input("Enter first number: "))  # Use float for division to handle decimal numbers
        num2 = float(input("Enter second number: "))  # Use float for division to handle decimal numbers

        if choice == 'A':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == 'S':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == 'M':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == 'D':
            try:
                print(num1, "/", num2, "=", divide(num1, num2))
            except ValueError as e:
                print("Error:", e)

        another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if another_calculation != 'yes':
            break
    else:
        print("Invalid Input. Please enter A, S, M, or D.")
