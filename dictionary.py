import json

# Load the JSON data containing word definitions
with open("dictionary.json", "r") as file:
    data = json.load(file)

def get_definitions(text):
    """
    Retrieves definitions for input words from the loaded JSON data.

    Args:
    text (str): Input text containing words for which definitions are needed.

    Returns:
    str: Definitions for the input words.
    """
    # Split the input text into individual words
    words = text.split()
    result = []  # Initialize an empty list to store the definitions
    
    # Iterate over each word in the input text
    for word in words:
        if word in data:  # Check if the word exists in the loaded JSON data
            result.append(data[word])  # Append the definition to the result list
        else:
            result.append("{}".format(word))  # If the word is not found, append the word itself
    
    # Join the elements of the result list into a single string and return it
    return ' '.join(result)

def provide_definitions(text, depth=0, max_depth=1):
    """
    Recursively provides definitions for input text.

    Args:
    text (str): Input text for which definitions are needed.
    depth (int): Current depth of recursion.
    max_depth (int): Maximum depth allowed for recursion.

    Returns:
    None
    """
    if depth > max_depth:
        return
    
    # Call the get_definitions function to retrieve definitions for the input text
    definitions = get_definitions(text)
    print("AI: {}".format(definitions))
    
    # Use the definitions as new input for the program
    new_input = definitions
    
    # Recursively call the provide_definitions function with the new input
    provide_definitions(new_input, depth + 1, max_depth)

# Prompt the user to input text to start the interaction
initial_input = input("You: ")
provide_definitions(initial_input)
