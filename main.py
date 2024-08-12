import streamlit as st
from add import add
from subtract import subtract
from multiply import multiply
from divide import divide

# Define the main function
def main():
    st.title("Simple Calculator")

    # Create a selectbox for operation choice
    operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide"])

    # Create input fields for numbers
    num1 = st.number_input("Enter first number:", format="%.2f")
    num2 = st.number_input("Enter second number:", format="%.2f")

    if st.button("Calculate"):
        if operation == "Add":
            result = add(num1, num2)
            operation_symbol = "+"
        elif operation == "Subtract":
            result = subtract(num1, num2)
            operation_symbol = "-"
        elif operation == "Multiply":
            result = multiply(num1, num2)
            operation_symbol = "*"
        elif operation == "Divide":
            try:
                result = divide(num1, num2)
                operation_symbol = "/"
            except ValueError as e:
                st.error(f"Error: {e}")
                result = None

        if result is not None:
            st.write(f"{num1} {operation_symbol} {num2} = {result}")

# Run the main function
if __name__ == "__main__":
    main()
