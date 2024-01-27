import streamlit as st

def main():
    st.title("Custom Greeting App")

    # Get user input for name
    name = st.text_input("Enter your name:")

    # Define the greeting variable
    var = v

    # Display personalized greeting
    if name:
        greeting_message = f"Hey, {name}! {var}"
        st.write(greeting_message)

if __name__ == "__main__":
    main()
