import json

# Load the JSON data containing word definitions
def load_dictionary(file_path):
    """
    Loads the dictionary data from a JSON file.

    Args:
    file_path (str): The path to the JSON file.

    Returns:
    dict: The loaded dictionary data.
    """
    with open(file_path, "r") as file:
        return json.load(file)

def get_definitions(text, dictionary):
    """
    Retrieves definitions for input words from the dictionary data.

    Args:
    text (str): Input text containing words for which definitions are needed.
    dictionary (dict): The dictionary data containing word definitions.

    Returns:
    str: Definitions for the input words.
    """
    # Split the input text into individual words
    words = text.split()
    result = []  # Initialize an empty list to store the definitions
    
    # Iterate over each word in the input text
    for word in words:
        # Check if the word exists in the dictionary
        if word in dictionary:
            result.append(dictionary[word])  # Append the definition to the result list
        else:
            result.append("{}".format(word))  # If the word is not found, append the word itself
    
    # Join the elements of the result list into a single string and return it
    return ' '.join(result)

def provide_definitions(text, dictionary, depth=0, max_depth=1):
    """
    Recursively provides definitions for input text.

    Args:
    text (str): Input text for which definitions are needed.
    dictionary (dict): The dictionary data containing word definitions.
    depth (int): Current depth of recursion.
    max_depth (int): Maximum depth allowed for recursion.

    Returns:
    None
    """
    if depth > max_depth:
        return
    
    # Call the get_definitions function to retrieve definitions for the input text
    definitions = get_definitions(text, dictionary)
    
    # If at the maximum depth, print the definitions
    if depth == max_depth:
        print("AI: {}".format(definitions))
    
    # Use the definitions as new input for the program
    new_input = definitions
    
    # Recursively call the provide_definitions function with the new input
    provide_definitions(new_input, dictionary, depth + 1, max_depth)

# Continuous interaction loop
def main():
    # File path to the dictionary JSON file
    file_path = "dictionary.json"
    
    # Load the dictionary data
    dictionary = load_dictionary(file_path)
    
    # Prompt the user to input text to start the interaction
    while True:
        user_input = input("You: ")
        provide_definitions(user_input, dictionary)

if __name__ == "__main__":
    main()
