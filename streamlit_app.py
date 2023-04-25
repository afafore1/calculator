import streamlit as st

# Set page title
st.set_page_config(page_title='Calculator App')

# Define the calculator function
def calculator(num1, num2, operation):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    else:
        result = None
    return result

# Create a title for the app
st.title('Simple Calculator')

# Create text inputs for the user to enter numbers
num1 = st.number_input('Enter the first number:', step=1)
num2 = st.number_input('Enter the second number:', step=1)

# Create a dropdown menu for the user to select the operation
operation = st.selectbox('Select the operation:', ['+', '-', '*', '/'])

# Call the calculator function with the user inputs and display the result
if st.button('Calculate'):
    result = calculator(num1, num2, operation)
    if result is not None:
        st.success(f'The result of {num1} {operation} {num2} is {result:.2f}')
    else:
        st.error('Invalid operation selected')
