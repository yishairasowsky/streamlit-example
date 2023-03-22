import streamlit as st
import re

def generate_response(input_text):
    # Generate some response based on input text
    response = f"You said: {input_text}. What would you like me to do next?"
    return response

def get_next_responses(response):
    # Split the response into segments based on numeric values
    numbers = re.findall(r'\d+', response)
    segments = re.split(r'\d+\.', response)
    reply, suggestions = segments[0], segments[1:]
    responses = {}
    for i in range(len(numbers)):
        responses[numbers[i]] = suggestions[i].strip()
    return responses

def main():
    # Define initial user input
    user_input = st.text_input("Enter some text here:")

    # Loop to continue conversation until user cancels or terminates
    while user_input:
        # Generate response based on user input
        response = generate_response(user_input)
        # Get next set of responses from the user via buttons
        next_responses = get_next_responses(response)
        # Create buttons for each response option
        button_container = st.container()
        cols = {}
        with button_container:
            cols['1'], cols['2'], cols['3'] = st.columns(3)
            for key, val in next_responses.items():
                if cols[key].button(next_responses[key]):
                    user_input = val
                    break
            else:
                user_input = None

if __name__ == "__main__":
    main()
