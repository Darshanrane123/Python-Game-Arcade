# Simple chatbot using if-else statements
def chatbot_response(message):
    # Convert the message to lowercase to make it case insensitive
    message = message.lower ( )

    # Define some predefined patterns and responses
    if message in ['hi' , 'hello' , 'hey' , 'hola']:
        return "Hello there! How can I help you today?"
    elif 'weather' in message:
        return "The weather is nice today."
    elif 'bye' in message:
        return "Goodbye! Have a nice day."
    else:
        return "Sorry, I don't understand that. Could you please rephrase?"


# Main function to run the chatbot
def main():
    print ( "Welcome! Ask me something or just say hi." )

    while True:
        user_input = input ( "You: " )
        if user_input.lower ( ) == 'exit':
            print ( "Chatbot: Goodbye!" )
            break

        response = chatbot_response ( user_input )
        print ( "Chatbot:" , response )


if __name__ == "__main__":
    main ( )

