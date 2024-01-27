import streamlit as st

def main():
    st.title("Greeting App")
    
    # Get user input for name
    name = st.text_input("Enter your name:")
    
    # Display greeting
    if name:
        st.write(f"Hey, {name}!")

if __name__ == "__main__":
    main()
