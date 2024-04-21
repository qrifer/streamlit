
import streamlit as st

def largest_number(a, b, c):
    return max(a, b, c)

def main():
    st.title("Find the Largest Number")

    # Input fields for three numbers
    number1 = st.number_input("Enter the first number", value=0)
    number2 = st.number_input("Enter the second number", value=0)
    number3 = st.number_input("Enter the third number", value=0)

    # Button to calculate the largest number
    if st.button("Find Largest Number"):
        largest = largest_number(number1, number2, number3)
        st.success(f"The largest number is: {largest}")

if __name__ == "__main__":
    main()
