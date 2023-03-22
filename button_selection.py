import streamlit as st

def main():
    st.title("Button Selection App")
    
    user_input = st.text_input("Enter your input:")
    button_options = {}
    
    while user_input:
        if len(button_options) == 0:
            button_options[user_input] = ["Option 1", "Option 2", "Option 3"]
        else:
            last_input = list(button_options.keys())[-1]
            last_button_choice = button_options[last_input].index(user_input)
            new_input_key = f"{last_input} - {user_input}"
            button_options[new_input_key] = [f"{new_input_key} - Option {i+1}" for i in range(3)]
        
        button_choice = st.button("Select an option", key=user_input)
        
        if button_choice:
            button_options_keys = list(button_options.keys())
            last_button_choice = button_options_keys.index(user_input)
            next_options = button_options[button_options_keys[last_button_choice+1]]
            next_input = st.selectbox("Choose an option", options=next_options)
            user_input = next_input
        else:
            break
    
    st.write("Thanks for using the Button Selection App!")
