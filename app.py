import streamlit as st

# Title of the app
st.title("🧮 Simple Calculator")

# Input numbers
st.header("Enter Numbers")
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Operation selection
st.header("Select Operation")
operation = st.selectbox(
    "Choose an operation",
    ("Addition", "Subtraction", "Multiplication", "Division")
)

# Calculate button
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.success(f"The result of addition is: {result}")
    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"The result of subtraction is: {result}")
    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"The result of multiplication is: {result}")
    elif operation == "Division":
        if num2 == 0:
            st.error("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            st.success(f"The result of division is: {result}")
