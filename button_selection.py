import streamlit as st

def main():
    st.title("Button Selection App")
    
    # Define the initial set of user inputs and button options
    user_input = st.text_input("Enter your input:")
    button_options = ["Option 1", "Option 2", "Option 3"]
    
    while user_input:
        # Display the current user input
        st.write(f"Current input: {user_input}")
        
        # Display the button options for the current user input
        for i in range(3):
            button_choice = st.button(f"{button_options[i]}")
            if button_choice:
                user_input_value = user_input + f" - {button_options[i]}"
                break
        
        # Ask for a new user input and reset the button options
        new_user_input = st.text_input("Enter your input:", value=user_input_value[len(user_input.split()[-1]):].strip())
        button_options = ["Option 1", "Option 2", "Option 3"]
        
        # Update the user input variable
        user
