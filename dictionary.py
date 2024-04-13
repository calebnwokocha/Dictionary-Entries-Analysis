import json
import random
import string

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

def get_definitions(word, dictionary):
    """
    Retrieves definitions for a single word from the dictionary data.

    Args:
    word (str): The word for which the definition is needed.
    dictionary (dict): The dictionary data containing word definitions.

    Returns:
    str: The definition of the word.
    """
    word = word.strip(string.punctuation).lower()
    if word in dictionary:
        return dictionary[word]
    else:
        return "{}".format(word)

def provide_definitions(text, dictionary, depth=0, max_depth=2):
    """
    Recursively provides definitions for input text.

    Args:
    text (str): Input text for which definitions are needed.
    dictionary (dict): The dictionary data containing word definitions.
    depth (int): Current depth of recursion.
    max_depth (int): Maximum depth allowed for recursion.

    Returns:
    str: The combined output containing definitions.
    """
    if depth > max_depth:
        return
    
    # Split the input text into individual words
    words = text.split()
    num_words = len(words)
    
    # Randomly select k words
    k = min(random.randint(1, num_words), num_words)  # Ensure k is not greater than the number of words
    print("Selected {} words for definitions.".format(k))
    selected_positions = random.sample(range(num_words), k)
    
    # Extract the selected words and their positions
    selected_words = [words[i] for i in selected_positions]
    selected_definitions = [get_definitions(word, dictionary) for word in selected_words]
    
    # Combine selected words with their definitions and unselected words while preserving positions
    combined_output = []
    for i, word in enumerate(words):
        if word in selected_words:
            # Append the definition of the selected word
            combined_output.append(selected_definitions[selected_words.index(word)])
        else:
            # Append the original word
            combined_output.append(word)
    
    # If at the maximum depth, return the definitions
    if depth == max_depth:
        print("AI: {}".format(' '.join(combined_output)))
        return ' '.join(combined_output)
    
    # Use the definitions as new input for the program
    new_input = ' '.join(combined_output)
    
    # Recursively call the provide_definitions function with the new input and return its result
    return provide_definitions(new_input, dictionary, depth + 1, max_depth)

# Continuous interaction loop
def main():
    # File path to the dictionary JSON file
    file_path = "dictionary.json"
    
    # Load the dictionary data
    dictionary = load_dictionary(file_path)
    
    # Prompt the user to input text to start the interaction
    while True:
        user_input = input("You: ")
        print("Providing definitions for input...")
        provide_definitions(user_input, dictionary)

if __name__ == "__main__":
    main()
