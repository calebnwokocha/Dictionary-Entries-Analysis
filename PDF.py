import PyPDF2 # type: ignore
import dictionary

def read_pdf(file_path):
    """
    Reads text from a PDF file.

    Args:
    file_path (str): The path to the PDF file.

    Returns:
    str: The text extracted from the PDF.
    """
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        text = ''
        for page_number in range(num_pages):
            page = pdf_reader.pages[page_number]
            text += page.extract_text()
        return text

def save_to_txt(text, output_txt_path):
    """
    Saves text to a text file.

    Args:
    text (str): The text to be saved to the text file.
    output_txt_path (str): The path to save the output text file.

    Returns:
    None
    """
    # Check if the text is None or empty
    if text is None or not text.strip():
        print("Error: No text to write to the text file.")
        return

    try:
        # Create or overwrite the text file
        with open(output_txt_path, 'w') as file:
            # Write the text to the file
            file.write(text)
        
        print("Text saved to:", output_txt_path)

    except Exception as e:
        print("An error occurred while saving the text file:", str(e))


def main():
    # Path to the PDF file
    pdf_file_path = "pvsnp.pdf"
    
    # Read the PDF file and extract all text
    pdf_text = read_pdf(pdf_file_path)
    
    # Load the dictionary data
    dictionary_file_path = "dictionary.json"
    dictionary_data = dictionary.load_dictionary(dictionary_file_path)
    
    # Provide definitions for the extracted text using the loaded dictionary data
    print("Providing definitions for text from PDF...")
    definitions_text = dictionary.provide_definitions(pdf_text, dictionary_data)
    print(definitions_text)

    # Save the definitions as a PDF file
    output_txt_path = "pvsnp_definitions_output.txt"
    save_to_txt(definitions_text, output_txt_path)
    print("Definitions saved to:", output_txt_path)

if __name__ == "__main__":
    main()