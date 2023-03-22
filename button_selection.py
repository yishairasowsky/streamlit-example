import streamlit as st

def main():
    st.title("Button Selection App")
    
    # Define the initial set of user inputs and button options
    user_inputs = st.text_input("Enter your input:", key="user_inputs").split("\n")
    button_options = ["Option 1", "Option 2", "Option 3"]
    
    for i, user_input in enumerate(user_inputs):
        if user_input.strip() == "":
            continue
        
        # Display the current user input
        st.write(f"Current input: {user_input}")
        
        # Display the button options for the current user input
        for j in range(3):
            button_choice = st.button(f"{button_options[j]}", key=f"{i}-{j}")
            if button_choice:
                user_inputs[i] = f"{user_input} - {button_options[j]}"
                break
        
        # Add a new input bar if this is not the last iteration
        if i != len(user_inputs) - 1:
            user_inputs[i+1] = st.text_input("Enter your input:", value=user_inputs[i+1], key=f"user_input_{i+1}").strip()
        
        # Reset the button options
        button_options = ["Option 1", "Option 2", "Option 3"]
    
    # Join the user inputs and write the final message
    final_input = "\n".join(user_inputs).strip()
    st.write(f"Final input: {final_input}")
    st.write("Thanks for using the Button Selection App!")

if __name__ == "__main__":
    main()
