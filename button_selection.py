import streamlit as st

def main():
    st.title("Button Selection App")

    # Define the initial user input
    user_input = st.text_input("Enter your input:")

    while user_input:
        # Display the current user input
        st.write(f"Current input: {user_input}")

        # Display a set of three buttons for the current input
        for i in range(3):
            button_choice = st.button(f"{user_input} - Option {i+1}")
            if button_choice:
                user_input = f"{user_input} - Option {i+1}"
                break

        # Ask for a new user input
        user_input = st.text_input("Enter your input:", value=user_input[len(user_input.split()[-1]):].strip())

    st.write("Thanks for using the Button Selection App!")

if __name__ == "__main__":
    main()
